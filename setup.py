#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")

requires = ["elasticsearch==7.5.1", "click==7.0"]


def get_version():
    init = open(os.path.join(ROOT, "eslog", "release.py")).read()
    return VERSION_RE.search(init).group(1)


setup(
    name="eslog",
    version=get_version(),
    author="Marius Stanca",
    author_email=["me@mariuss.me"],
    url="https://github.com/wmariuss/eslog",
    license="BSD 3-Clause",
    description="Get and send logs.",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={"": ["README.md"]},
    install_requires=requires,
    extras_require={"click": ["click==7.0"]},
    zip_safe=False,
    classifiers=[
        "Environment :: Tools",
        "Intended Audience :: Operations",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.x",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points="""
        [console_scripts]
        eslog=eslog.main:cli
    """,
)
