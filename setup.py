import os
import re
import shutil

from setuptools import find_packages, setup

setup(
    name="robotnavigation",
    version="1.0.0.dev0",
    author="tronguyen",
    author_email="trongnt.cs@gmail.com",
    description="Assignment Robot Navigation",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/trongntcs/robot_navigation.git",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.6.0",
    install_requires=[
        "pytest",
    ],
)