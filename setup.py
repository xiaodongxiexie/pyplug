# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/6

from setuptools import setup, find_packages
from pyplug import __title__, __version__, __description__, __author__, __author_email__

def long_description():
    with open("README.md", encoding="utf-8") as file:
       description = file.read()
    return description


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=long_description(),
    url="https://github.com/xiaodongxiexie/pyplug",
    author=__author__,
    author_email=__author_email__,
    data_files=[
        ("example", [
            "example/simple.py",
        ]),
        ("test", [
            "test/test_plug.py",
                ]),
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    keywords="plug",
)
