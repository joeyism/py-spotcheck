# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('checkspot/checkspot.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

with open("requirements.txt", "rb") as f:
    req = f.read().decode("utf-8")


setup(
    name = "checkspot",
    packages = ["checkspot"],
    entry_points = {
        "console_scripts": ['checkspot = checkspot.checkspot:main']
        },
    version = version,
    description = "A simple CLI tool to check the spot prices of AWS instances. ",
    long_description = long_descr,
    author = "Joey Sham",
    author_email = "sham.joey@gmail.com",
    url = "http://www.joeyism.com",
    install_requires=req
    )
