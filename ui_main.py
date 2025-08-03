# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPpOtOP.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1110, 691)
        MainWindow.setMinimumSize(QSize(1080, 0))
        MainWindow.setStyleSheet(u"/* Soft Dark Theme for PySide6 UI */\n"
"\n"
"QWidget {\n"
"    background-color: #23272e;\n"
"    color: #e0e0e0;\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #23272e;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: #262b33;\n"
"    border: 1px solid #353b45;\n"
"    border-radius: 6px;\n"
"    margin-top: 10px;\n"
"    color: #e0e0e0;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #4CAF50;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2d323b;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #353b45;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3a3f4b;\n"
"    border: 1px solid #4CAF50;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButto"
                        "n:pressed {\n"
"    background-color: #23272e;\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QTextEdit {\n"
"    background-color: #23272e;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #353b45;\n"
"    border-radius: 4px;\n"
"    selection-background-color: #4CAF50;\n"
"    selection-color: #23272e;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #e0e0e0;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #4CAF50;\n"
"    background: #23272e;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #4CAF50;\n"
"    background: #4CAF50;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #23272e;\n"
"    color: #e0e0e0;\n"
"    border: 1px solid #353b45;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #23272e;\n"
"    color: #e0e0e0;\n"
"    border"
                        ": 1px solid #353b45;\n"
"    selection-background-color: #4CAF50;\n"
"    selection-color: #23272e;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.top_layout = QVBoxLayout()
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(0, -1, 0, -1)
        self.project_group = QGroupBox(self.centralwidget)
        self.project_group.setObjectName(u"project_group")
        self.project_group.setMinimumSize(QSize(0, 125))
        self.project_group.setMaximumSize(QSize(16777215, 165))
        self.project_layout = QGridLayout(self.project_group)
        self.project_layout.setObjectName(u"project_layout")
        self.project_layout.setContentsMargins(10, 10, 10, 5)
        self.frame_2 = QFrame(self.project_group)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 45))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.app_name_label = QLabel(self.frame_2)
        self.app_name_label.setObjectName(u"app_name_label")

        self.horizontalLayout_2.addWidget(self.app_name_label)

        self.app_name = QLineEdit(self.frame_2)
        self.app_name.setObjectName(u"app_name")

        self.horizontalLayout_2.addWidget(self.app_name)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.app_icon_label = QLabel(self.frame_2)
        self.app_icon_label.setObjectName(u"app_icon_label")

        self.horizontalLayout_2.addWidget(self.app_icon_label)

        self.app_icon = QPushButton(self.frame_2)
        self.app_icon.setObjectName(u"app_icon")
        self.app_icon.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.app_icon)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.package_name_label = QLabel(self.frame_2)
        self.package_name_label.setObjectName(u"package_name_label")

        self.horizontalLayout_2.addWidget(self.package_name_label)

        self.package_name = QLineEdit(self.frame_2)
        self.package_name.setObjectName(u"package_name")

        self.horizontalLayout_2.addWidget(self.package_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.version_label = QLabel(self.frame_2)
        self.version_label.setObjectName(u"version_label")

        self.horizontalLayout_2.addWidget(self.version_label)

        self.version = QLineEdit(self.frame_2)
        self.version.setObjectName(u"version")

        self.horizontalLayout_2.addWidget(self.version)


        self.project_layout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(self.project_group)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 45))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.project_path_label = QLabel(self.frame)
        self.project_path_label.setObjectName(u"project_path_label")

        self.horizontalLayout.addWidget(self.project_path_label)

        self.project_path = QLineEdit(self.frame)
        self.project_path.setObjectName(u"project_path")

        self.horizontalLayout.addWidget(self.project_path)

        self.browse_btn = QPushButton(self.frame)
        self.browse_btn.setObjectName(u"browse_btn")

        self.horizontalLayout.addWidget(self.browse_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.edit_spec_file = QCheckBox(self.frame)
        self.edit_spec_file.setObjectName(u"edit_spec_file")

        self.horizontalLayout.addWidget(self.edit_spec_file)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.project_layout.addWidget(self.frame, 2, 0, 1, 1)


        self.top_layout.addWidget(self.project_group)

        self.platform_group = QGroupBox(self.centralwidget)
        self.platform_group.setObjectName(u"platform_group")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.platform_group.sizePolicy().hasHeightForWidth())
        self.platform_group.setSizePolicy(sizePolicy)
        self.platform_group.setMinimumSize(QSize(0, 140))
        self.platform_group.setMaximumSize(QSize(16777215, 175))
        self.horizontalLayout_3 = QHBoxLayout(self.platform_group)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.linux_frame = QFrame(self.platform_group)
        self.linux_frame.setObjectName(u"linux_frame")
        self.linux_frame.setFrameShape(QFrame.Shape.Box)
        self.gridLayout_2 = QGridLayout(self.linux_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.linux_arch_label = QLabel(self.linux_frame)
        self.linux_arch_label.setObjectName(u"linux_arch_label")

        self.gridLayout_2.addWidget(self.linux_arch_label, 1, 0, 1, 1)

        self.linux_check = QCheckBox(self.linux_frame)
        self.linux_check.setObjectName(u"linux_check")
        self.linux_check.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.linux_check.setFont(font)

        self.gridLayout_2.addWidget(self.linux_check, 0, 0, 1, 3)

        self.linux_arch = QLabel(self.linux_frame)
        self.linux_arch.setObjectName(u"linux_arch")

        self.gridLayout_2.addWidget(self.linux_arch, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.linux_frame)

        self.android_armv7a_frame = QFrame(self.platform_group)
        self.android_armv7a_frame.setObjectName(u"android_armv7a_frame")
        self.android_armv7a_frame.setFrameShape(QFrame.Shape.Box)
        self.gridLayout_6 = QGridLayout(self.android_armv7a_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.android_armv7a_check = QCheckBox(self.android_armv7a_frame)
        self.android_armv7a_check.setObjectName(u"android_armv7a_check")
        self.android_armv7a_check.setMinimumSize(QSize(0, 30))
        self.android_armv7a_check.setFont(font)

        self.gridLayout_6.addWidget(self.android_armv7a_check, 0, 0, 1, 2)

        self.android_armv7a_label = QLabel(self.android_armv7a_frame)
        self.android_armv7a_label.setObjectName(u"android_armv7a_label")

        self.gridLayout_6.addWidget(self.android_armv7a_label, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.android_armv7a_frame)

        self.android_aarch64_frame = QFrame(self.platform_group)
        self.android_aarch64_frame.setObjectName(u"android_aarch64_frame")
        self.android_aarch64_frame.setFrameShape(QFrame.Shape.Box)
        self.gridLayout_7 = QGridLayout(self.android_aarch64_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.android_aarch64_check = QCheckBox(self.android_aarch64_frame)
        self.android_aarch64_check.setObjectName(u"android_aarch64_check")
        self.android_aarch64_check.setMinimumSize(QSize(0, 30))
        self.android_aarch64_check.setFont(font)

        self.gridLayout_7.addWidget(self.android_aarch64_check, 0, 0, 1, 2)

        self.android_aarch64_label = QLabel(self.android_aarch64_frame)
        self.android_aarch64_label.setObjectName(u"android_aarch64_label")

        self.gridLayout_7.addWidget(self.android_aarch64_label, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.android_aarch64_frame)

        self.android_x86_64_frame = QFrame(self.platform_group)
        self.android_x86_64_frame.setObjectName(u"android_x86_64_frame")
        self.android_x86_64_frame.setFrameShape(QFrame.Shape.Box)
        self.gridLayout_4 = QGridLayout(self.android_x86_64_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.android_x86_64_label = QLabel(self.android_x86_64_frame)
        self.android_x86_64_label.setObjectName(u"android_x86_64_label")

        self.gridLayout_4.addWidget(self.android_x86_64_label, 3, 0, 1, 1)

        self.android_x86_64_check = QCheckBox(self.android_x86_64_frame)
        self.android_x86_64_check.setObjectName(u"android_x86_64_check")
        self.android_x86_64_check.setMinimumSize(QSize(0, 30))
        self.android_x86_64_check.setFont(font)

        self.gridLayout_4.addWidget(self.android_x86_64_check, 0, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.android_x86_64_frame)

        self.android_i686_frame = QFrame(self.platform_group)
        self.android_i686_frame.setObjectName(u"android_i686_frame")
        self.android_i686_frame.setFrameShape(QFrame.Shape.Box)
        self.gridLayout_5 = QGridLayout(self.android_i686_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.android_i686_label = QLabel(self.android_i686_frame)
        self.android_i686_label.setObjectName(u"android_i686_label")

        self.gridLayout_5.addWidget(self.android_i686_label, 3, 0, 1, 1)

        self.android_i686_check = QCheckBox(self.android_i686_frame)
        self.android_i686_check.setObjectName(u"android_i686_check")
        self.android_i686_check.setMinimumSize(QSize(0, 30))
        self.android_i686_check.setFont(font)

        self.gridLayout_5.addWidget(self.android_i686_check, 0, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.android_i686_frame)


        self.top_layout.addWidget(self.platform_group)


        self.gridLayout.addLayout(self.top_layout, 1, 0, 2, 2)

        self.bottom_layout = QVBoxLayout()
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, -1, 0, -1)
        self.progress_group = QGroupBox(self.centralwidget)
        self.progress_group.setObjectName(u"progress_group")
        self.gridLayout_3 = QGridLayout(self.progress_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.log_label = QLabel(self.progress_group)
        self.log_label.setObjectName(u"log_label")

        self.gridLayout_3.addWidget(self.log_label, 0, 0, 1, 1)

        self.continue_btn = QPushButton(self.progress_group)
        self.continue_btn.setObjectName(u"continue_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.continue_btn.sizePolicy().hasHeightForWidth())
        self.continue_btn.setSizePolicy(sizePolicy1)
        self.continue_btn.setMinimumSize(QSize(50, 0))

        self.gridLayout_3.addWidget(self.continue_btn, 0, 1, 1, 1)

        self.log_text = QTextEdit(self.progress_group)
        self.log_text.setObjectName(u"log_text")
        sizePolicy.setHeightForWidth(self.log_text.sizePolicy().hasHeightForWidth())
        self.log_text.setSizePolicy(sizePolicy)
        self.log_text.setMaximumSize(QSize(16777215, 200))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.log_text.setFont(font1)

        self.gridLayout_3.addWidget(self.log_text, 1, 0, 1, 2)


        self.bottom_layout.addWidget(self.progress_group)

        self.control_layout = QHBoxLayout()
        self.control_layout.setObjectName(u"control_layout")
        self.build_all_btn = QPushButton(self.centralwidget)
        self.build_all_btn.setObjectName(u"build_all_btn")

        self.control_layout.addWidget(self.build_all_btn)

        self.build_selected_btn = QPushButton(self.centralwidget)
        self.build_selected_btn.setObjectName(u"build_selected_btn")

        self.control_layout.addWidget(self.build_selected_btn)

        self.cancel_btn = QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.control_layout.addWidget(self.cancel_btn)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.control_layout.addItem(self.horizontal_spacer)

        self.clear_log_btn = QPushButton(self.centralwidget)
        self.clear_log_btn.setObjectName(u"clear_log_btn")

        self.control_layout.addWidget(self.clear_log_btn)


        self.bottom_layout.addLayout(self.control_layout)


        self.gridLayout.addLayout(self.bottom_layout, 3, 0, 1, 2)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy2)
        self.title_label.setMinimumSize(QSize(0, 0))
        self.title_label.setMaximumSize(QSize(16777215, 60))
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.project_group.setStyleSheet(QCoreApplication.translate("MainWindow", "border:none;", None))
        self.project_group.setTitle(QCoreApplication.translate("MainWindow", "📂Project Configuration", None))
        self.app_name_label.setText(QCoreApplication.translate("MainWindow", "App Name:", None))
        self.app_name.setPlaceholderText(QCoreApplication.translate("MainWindow", "MyAwesomeApp", None))
        self.app_icon_label.setText(QCoreApplication.translate("MainWindow", "App Icon: ", None))
        self.app_icon.setText(QCoreApplication.translate("MainWindow", "📂 Browse", None))
        self.package_name_label.setText(QCoreApplication.translate("MainWindow", "Package name: ", None))
        self.package_name.setPlaceholderText(QCoreApplication.translate("MainWindow", "org.main.main", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", "Version:", None))
        self.version.setText(QCoreApplication.translate("MainWindow", "0.0.1", None))
        self.project_path_label.setText(QCoreApplication.translate("MainWindow", "Project Path:", None))
        self.project_path.setPlaceholderText(QCoreApplication.translate("MainWindow", "/path/to/your/pyside6/project", None))
        self.browse_btn.setText(QCoreApplication.translate("MainWindow", "📂 Browse", None))
        self.edit_spec_file.setText(QCoreApplication.translate("MainWindow", "✏️ Edit Spec File manually", None))
        self.platform_group.setTitle(QCoreApplication.translate("MainWindow", "🎯 Target Platforms", None))
        self.linux_arch_label.setText(QCoreApplication.translate("MainWindow", "Architecture:", None))
        self.linux_check.setText(QCoreApplication.translate("MainWindow", "🐧 Linux", None))
        self.linux_arch.setText(QCoreApplication.translate("MainWindow", "x86_64", None))
        self.android_armv7a_check.setText(QCoreApplication.translate("MainWindow", "🤖 Android", None))
        self.android_armv7a_label.setText(QCoreApplication.translate("MainWindow", "Architecture: armv7a", None))
        self.android_aarch64_check.setText(QCoreApplication.translate("MainWindow", "🤖 Android", None))
        self.android_aarch64_label.setText(QCoreApplication.translate("MainWindow", "Architecture: aarch64", None))
        self.android_x86_64_label.setText(QCoreApplication.translate("MainWindow", "Architecture: x86_64", None))
        self.android_x86_64_check.setText(QCoreApplication.translate("MainWindow", "🤖 Android", None))
        self.android_i686_label.setText(QCoreApplication.translate("MainWindow", "Architecture: i686", None))
        self.android_i686_check.setText(QCoreApplication.translate("MainWindow", "🤖 Android", None))
        self.progress_group.setTitle(QCoreApplication.translate("MainWindow", "📊 Build Progress", None))
        self.log_label.setText(QCoreApplication.translate("MainWindow", "📝 Build Log:", None))
        self.continue_btn.setText(QCoreApplication.translate("MainWindow", "▶️ Continue", None))
        self.build_all_btn.setStyleSheet(QCoreApplication.translate("MainWindow", """
QPushButton {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #45a049;
}
                """, None))
        self.build_all_btn.setText(QCoreApplication.translate("MainWindow", "🚀 Build All Platforms", None))
        self.build_selected_btn.setText(QCoreApplication.translate("MainWindow", "▶️ Build Selected", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", "❌ Cancel All", None))
        self.clear_log_btn.setText(QCoreApplication.translate("MainWindow", "🧹 Clear Log", None))
        self.title_label.setStyleSheet(QCoreApplication.translate("MainWindow", "color: #4CAF50; padding: 10px;", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", "Cross-Platform PySide6 Deployment Tool", None))
        pass
    # retranslateUi
