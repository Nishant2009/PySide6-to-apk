import shutil
import sys
from .ui_main import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QImage
from .build_Linux import LinuxDeploy
from .build_Android import AndroidDeploy
from pathlib import Path
from PySide6.QtCore import QThread, Signal

class BuildWorker(QThread):
    output = Signal(str)

    def __init__(self, stream_func):
        super().__init__()
        self.stream_func = stream_func

    def run(self):
        for line in self.stream_func():
            self.output.emit(line)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.icon_path = None
        self.dir_path = None

        # set click events
        self.app_icon.clicked.connect(self.change_icon)
        self.browse_btn.clicked.connect(self.select_project_dir)
        self.build_all_btn.clicked.connect(self.deploy_all)
        self.build_selected_btn.clicked.connect(self.deploy_selected)
        self.clear_log_btn.clicked.connect(lambda: self.log_text.clear())
        self.cancel_btn.clicked.connect(self.cancel_deployment)
        self.continue_btn.clicked.connect(self.continue_deployment)

    def change_icon(self):
        self.icon_path, _ = QFileDialog.getOpenFileName(self, "Select Icon", "", "Images (*.png *.jpg *jpeg *ico);;All Files (*)")
        if self.icon_path and QImage(self.icon_path).isNull() is False:
            self.app_icon.setIcon(QIcon(self.icon_path))
        else:
            QMessageBox.warning(self, "Invalid Image", "The selected file is not a valid image.")

    def select_project_dir(self):
        self.dir_path = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if self.dir_path:
            self.project_path.setText(self.dir_path)

    def check_fields(self):
        if not self.app_name.text() or not self.package_name.text() or not self.version.text() or not self.dir_path or not self.icon_path:
            QMessageBox.warning(self, "Missing Information", "Please fill in all required fields.")
            return False
        return True
    
    def continue_deployment(self):
        if not self.edit_spec_file.isChecked():
            QMessageBox.warning(self, "Never Paused to Edit Spec File", "Please check the 'Edit Spec File' option to continue.")
            return
        if self.dir_path:
            spec_file = Path(self.dir_path) / "buildozer.spec"  # Replace with actual spec file name logic
            if not spec_file.exists():
                QMessageBox.warning(self, "No Spec File", "Spec file not found. Please start the deployment first.")
                return
            continue_flag = Path(self.dir_path) / "continue.flag"
            continue_flag.touch()
            self.log_text.append("Continue flag created. Deployment should resume.")
        else:
            QMessageBox.warning(self, "Project Not Started", "Please at least start the deployment once.")

    def deploy_all(self):
        if not self.check_fields():
            return
        app_name = self.app_name.text().strip()
        package_name = self.package_name.text().strip()
        version = self.version.text().strip()
        project_dir = self.dir_path
        icon_path = self.icon_path

        self.log_text.append("Deploying for Linux...")
        linux_deployer = LinuxDeploy(
            app_name=app_name,
            app_icon=Path(icon_path),
            version=version,
            project_dir=Path(project_dir)
        )
        self.linux_worker = BuildWorker(linux_deployer.build_executable_stream)
        self.linux_worker.output.connect(self.log_text.append)
        self.linux_worker.start()

        # Deploy for all Android architectures
        self.android_workers = []
        for arch in ["armv7a", "aarch64", "i686", "x86_64"]:
            android_deployer = AndroidDeploy(
                platform=arch,
                app_name=app_name,
                app_icon=Path(icon_path),
                package_name=package_name,
                version=version,
                edit_manually=self.edit_manually.isChecked(),
                project_dir=Path(project_dir)
            )
            worker = BuildWorker(android_deployer.deploy_stream)
            worker.output.connect(self.log_text.append)
            worker.start()
            self.android_workers.append(worker)

        # collect back the APK files from parent directory/dist by moving dist to current folder
        shutil.move(Path(self.dir_path).parent / "dist", Path(self.dir_path) / "dist") if (Path(self.dir_path).parent / "dist").exists() else None

    def deploy_selected(self):
        self.deploy_queue = []
        self.deploy_widgets = []  # To keep track of which widget to update

        if self.linux_check.isChecked():
            if not self.app_name.text() or not self.version.text() or not self.dir_path or not self.icon_path:
                QMessageBox.warning(self, "Missing Information", "Please fill in all required fields.")
                return
            linux_deployer = LinuxDeploy(
                app_icon=Path(self.icon_path),
                app_name=self.app_name.text().strip(),
                version=self.version.text().strip(),
                project_dir=Path(self.dir_path)
            )
            self.deploy_queue.append(linux_deployer.build_executable_stream)
            self.deploy_widgets.append(self.linux_check)

        android_targets = [
            ("android_armv7a_check", "armv7a"),
            ("android_aarch64_check", "aarch64"),
            ("android_x86_64_check", "x86_64"),
            ("android_i686_check", "i686"),
        ]

        for check_attr, arch in android_targets:
            widget = getattr(self, check_attr)
            if widget.isChecked():
                if not self.check_fields():
                    return
                android_deployer = AndroidDeploy(
                    platform=arch,
                    app_name=self.app_name.text().strip(),
                    app_icon=Path(self.icon_path),
                    package_name=self.package_name.text().strip(),
                    version=self.version.text().strip(),
                    edit_manually=self.edit_spec_file.isChecked(),
                    project_dir=Path(self.dir_path)
                )
                self.deploy_queue.append(android_deployer.deploy_stream)
                self.deploy_widgets.append(widget)

        if not self.deploy_queue:
            QMessageBox.warning(self, "No Deployment Option Selected", "Please select at least one deployment option.")
            return

        self.run_next_deploy()

        # collect back the APK files from parent directory/dist by moving dist to current folder
        shutil.move(Path(self.dir_path).parent / "dist", Path(self.dir_path) / "dist") if (Path(self.dir_path).parent / "dist").exists() else None

    def run_next_deploy(self):
        if not self.deploy_queue:
            self.log_text.append("All selected deployments finished.")
            self.current_worker = None
            return
        stream_func = self.deploy_queue.pop(0)
        self.current_widget = self.deploy_widgets.pop(0)
        self.current_worker = BuildWorker(stream_func)
        self.current_worker.output.connect(self.log_text.append)
        self.current_worker.finished.connect(self.on_deploy_finished)
        self.current_worker.start()

    def on_deploy_finished(self):
        text = self.current_widget.text()
        if "✅" not in text:
            self.current_widget.setText(f"{text} ✅")
        self.run_next_deploy()

    def cancel_deployment(self):
        shutil.move(Path(self.dir_path).parent / "dist", Path(self.dir_path) / "dist") if (Path(self.dir_path).parent / "dist").exists() else None
        if hasattr(self, "linux_worker"):
            self.linux_worker.terminate()
        if hasattr(self, "android_workers"):
            for worker in self.android_workers:
                worker.terminate()
        if hasattr(self, "current_worker") and self.current_worker is not None:
            self.current_worker.terminate()
        self.log_text.append("Deployment cancelled.")

def main():
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()