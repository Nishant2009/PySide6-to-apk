import os
import tempfile
import sys
import shutil
import subprocess
import urllib.request
from git import Repo
import importlib.util
from pathlib import Path
# Make sure GitPython and PySide6 are installed: pip install GitPython PySide6

HOME_DIR = Path.home()
PYSIDE6_ANDROID_DEPLOY = HOME_DIR / ".pyside6_android_deploy"

def pip_install_requirement(requirement):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirement])


class AndroidSetup:
    def __init__(self):
        self.pyside_repo_path = os.path.join(HOME_DIR, "pyside-setup")
        self.ensure_libclang()
        self.ensure_pyside_android_deploy()

    def ensure_pyside_android_deploy(self):
        if os.path.exists(PYSIDE6_ANDROID_DEPLOY):
            return
        if not os.path.exists(self.pyside_repo_path):
            Repo.clone_from("https://code.qt.io/pyside/pyside-setup", self.pyside_repo_path)
            self.download_sdk_ndk()
            self.download_pyside_wheels()
            self.edit_PySide6_android_deploy()

    def edit_PySide6_android_deploy(self):
        spec = importlib.util.find_spec("PySide6.scripts.android_deploy")
        android_deploy_path = spec.origin
        spec_editor = Path(__file__).parent / "spec_editor.txt"
        print(f"Editing {android_deploy_path} with {spec_editor}")

        with open(android_deploy_path, "r") as file:
            lines = file.readlines()

        with open(spec_editor, "r") as file:
            insert_content = file.readlines()

        content = lines[:128] + ["        edit_specs()\n"] + lines[128:]
        content = content[:51] + insert_content + content[51:]

        with open(android_deploy_path, "w") as file:
            file.writelines(content)

    def ensure_libclang(self):
        if os.environ.get("LLVM_INSTALL_DIR"):
            return
        url = "https://download.qt.io/development_releases/prebuilt/libclang/libclang-release_140-based-linux-Rhel8.2-gcc9.2-x86_64.7z"
        with tempfile.TemporaryDirectory() as tmpdir:
            archive_path = os.path.join(tmpdir, "libclang.7z")
            # Download the file
            urllib.request.urlretrieve(url, archive_path)
            # Extract to home directory
            os.system(f"7z x {archive_path} -o{self.home_dir}")

        llvm_dir = os.path.join(os.getcwd(), "libclang")
        os.environ["LLVM_INSTALL_DIR"] = llvm_dir

        shell = os.environ.get("SHELL")
        if "zsh" in shell:
            rc_file = os.path.join(self.home_dir, ".zshrc")
        elif "bash" in shell:
            rc_file = os.path.join(self.home_dir, ".bashrc")
        else:
            rc_file = None

        if rc_file:
            with open(rc_file, "a") as f:
                f.write(f'\nexport LLVM_INSTALL_DIR="{llvm_dir}"\n')
                
    def download_pyside_wheels(self):
        wheels_dir = PYSIDE6_ANDROID_DEPLOY / "wheels"
        wheels_dir.mkdir(parents=True, exist_ok=True)

        # Download PySide6 and Shiboken6 wheels
        architectures = ["armv7a", "aarch64", "i686", "x86_64"]
        for arch in architectures:
            pyside_wheel_url = f"https://github.com/EchterAlsFake/PySide6-to-Android/releases/download/6.8.0_3.11/PySide6-6.8.0-6.8.0-cp311-cp311-android_{arch}.whl"
            shiboken_wheel_url = f"https://github.com/EchterAlsFake/PySide6-to-Android/releases/download/6.8.0_3.11/shiboken6-6.8.0-6.8.0-cp311-cp311-android_{arch}.whl"

            urllib.request.urlretrieve(pyside_wheel_url, wheels_dir / f"PySide6-6.8.0-6.8.0-cp311-cp311-android_{arch}.whl")
            urllib.request.urlretrieve(shiboken_wheel_url, wheels_dir / f"shiboken6-6.8.0-6.8.0-cp311-cp311-android_{arch}.whl")
        subprocess.check_call(["chmod", "+x", "*"], cwd=wheels_dir)

    def download_sdk_ndk(self):
        os.chdir(self.pyside_repo_path)
        pip_install_requirement(Path("requirements.txt"))
        pip_install_requirement(Path("tools/cross_compile_android/requirements.txt").resolve())
        subprocess.check_call(["python", "tools/cross_compile_android/main.py", "--download-only", "--auto-accept-license"])
        os.chdir(HOME_DIR)
        shutil.rmtree(self.pyside_repo_path, ignore_errors=True)


class AndroidDeploy:
    def __init__(self, platform: str = "armv7a", app_name: str = "MyApp", app_icon: Path = Path.cwd() / "icon.png", package_name: str = "com.example.myapp", version: str = "0.0.1", edit_manually: bool = False, project_dir: Path = None):
        self.setup = AndroidSetup()
        if project_dir is None:
            project_dir = Path.cwd()
        self.project_dir = project_dir.resolve()
        self.app_name = app_name
        self.app_icon = app_icon
        self.package_name = package_name
        self.version = version
        self.edit_manually = edit_manually
        self.ndk_path = PYSIDE6_ANDROID_DEPLOY / "android-ndk" / "android-ndk-r27c"
        self.sdk_path = PYSIDE6_ANDROID_DEPLOY / "android-sdk"
        self.wheel_pyside = PYSIDE6_ANDROID_DEPLOY / "wheels" / f"PySide6-6.8.0-6.8.0-cp311-cp311-android_{platform}.whl"
        self.wheel_shiboken = PYSIDE6_ANDROID_DEPLOY / "wheels" / f"shiboken6-6.8.0-6.8.0-cp311-cp311-android_{platform}.whl"

    @staticmethod
    def run_command_stream(cmd, cwd=None):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, cwd=cwd)
        for line in process.stdout:
            yield line
        process.wait()
        yield f"Process finished with code: {process.returncode}\n"

    def deploy_stream(self):
        os.chdir(self.project_dir)
        os.remove("auto_values.txt") if os.path.exists("auto_values.txt") else None
        os.remove("continue.flag") if os.path.exists("continue.flag") else None
        with open("auto_values.txt", "w") as f:
            f.write(f"title={self.app_name}\n")
            f.write(f"icon_path={self.app_icon}\n")
            f.write(f"package={self.package_name}\n")
            f.write(f"version={self.version}\n")
            f.write(f"edit_manually={1 if self.edit_manually else 0}\n")

        deploy_command = [
            "pyside6-android-deploy",
            f"--wheel-pyside={self.wheel_pyside}",
            f"--wheel-shiboken={self.wheel_shiboken}",
            "--name", "MyApp",
            "--ndk-path", self.ndk_path,
            "--sdk-path", self.sdk_path,
            "--force",
        ]

        yield from self.run_command_stream(deploy_command)

        apk_files = list(self.project_dir.glob("*.apk"))
        if apk_files:
            apk_file = apk_files[0]
            destination = self.project_dir.parent / "dist" / apk_file.name
            shutil.move(apk_file, destination)
            yield f"Temporary moving APK to {destination}\n"
        os.remove("continue.flag") if os.path.exists("continue.flag") else None
        os.remove("auto_values.txt") if os.path.exists("auto_values.txt") else None



if __name__ == "__main__":
    deployer = AndroidDeploy(
        platform="armv7a",
        app_name="My Application",
        app_icon=Path.cwd().parent / "TEST_PySide6_2_APK" / "icon.jpg",
        package_name="com.my.test",
        version="0.1.0",
        edit_manually=True,
        project_dir=Path.cwd().parent / "TEST_PySide6_2_APK"
    )
    deployer.deploy()