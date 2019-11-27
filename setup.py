# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# load env
from dotenv import load_dotenv
load_dotenv()

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="TTM_Streamer",
    version="0.1.0",
    description="TTM Data Streamer and Order book manager",
    license="MIT",
    author="Raphael THIBIERGE",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ]
)
