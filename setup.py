from setuptools import setup, find_packages

with open("ReadMe.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PySide6-to-apk",
    version="1.0.0",
    description="Effortlessly build and package your PySide6 apps for Linux and Android apks — no command-line struggles, just a beautiful GUI!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nishant Pratap Savita",
    url="https://github.com/Nishant2009/PySide6-to-apk",
    project_urls={
        "Source": "https://github.com/Nishant2009/PySide6-to-apk",
        "Tracker": "https://github.com/Nishant2009/PySide6-to-apk/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PySide6",
        "PyInstaller",
        "GitPython"
    ],
    entry_points={
        "console_scripts": [
            "PySide6-to-apk=pyside6_to_apk.main:main"
        ]
    },
    package_data={
        "": ["*.ui", "*.txt", "*.spec", "*.jpg", "*.png"]
    },
    python_requires=">=3.10",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Natural Language :: English",
    ],
)