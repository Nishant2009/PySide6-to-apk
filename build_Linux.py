from pathlib import Path
import shutil
import subprocess
import sys
import os


class LinuxSetup:
    def __init__(self):
        # check if pyinstaller is installed
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "show", "PyInstaller"], 
                                 stdout=subprocess.DEVNULL, 
                                 stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "PyInstaller"])
            except subprocess.CalledProcessError as e:
                yield f"Failed to install PyInstaller: {e}"
                return
            yield "PyInstaller installed successfully."

class LinuxDeploy:
    def __init__(self, app_name: str = "MyApp", app_icon: Path = Path.cwd() / "icon.png", version: str = "0.0.1", project_dir: Path = None):
        self.setup = LinuxSetup()
        if project_dir is None:
            project_dir = Path.cwd()
        self.project_dir = project_dir.resolve()
        self.app_name = app_name
        self.app_icon = app_icon
        self.version = version

    def collect_add_data_args(self,base_dir):
        add_data_args = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, base_dir)
                # Format: source:destination
                add_data_args.append(f"{abs_path}:{rel_path}")
        return add_data_args

    @staticmethod
    def run_command_stream(cmd, cwd=None):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, cwd=cwd)
        for line in process.stdout:
            yield line
        process.wait()
        yield f"Process finished with code: {process.returncode}\n"

    def build_executable_stream(self):
        os.chdir(self.project_dir)
        base_dir = self.project_dir
        main_script = os.path.join(base_dir, "main.py")
        add_data_args = self.collect_add_data_args(base_dir)

        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--clean",  # Clean build files
            f"--icon={self.app_icon}",
            f"--name={self.app_name}",
            f"--distpath={self.project_dir.parent / 'dist'}",  # Replace with your desired output folder
            main_script
        ]

        for data in add_data_args:
            if data.startswith(main_script):
                continue
            cmd.extend(["--add-data", data])

        yield from self.run_command_stream(cmd)

        shutil.rmtree(self.project_dir / "build", ignore_errors=True)


if __name__ == "__main__":
    deployer = LinuxDeploy(
        app_name="MyApp",
        app_icon=Path("../TEST_PySide6_2_APK/icon.jpg").absolute(),
        version="0.0.1",
        project_dir=Path("../TEST_PySide6_2_APK").absolute()
    )
    deployer.build_executable()