# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/8/6

from setuptools import setup, find_packages
from pyplug import __author__, __author_email__, __version__, __title__, __description__


def long_description():
    description = ""
    return description


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=long_description(),
    url="",
    author=__author__,
    author_email=__author_email__,
    data_files=[
        ("example", [
            "example/simple.py",
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
