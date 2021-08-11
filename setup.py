#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = ["antlr4-python3-runtime"]

test_requirements = []

setup(
    author="Arun Sharma",
    author_email="arun@sharma-home.net",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Java to Python Transpiler",
    entry_points={"console_scripts": ["decaf2many=decaf2many.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="decaf2many",
    name="decaf2many",
    packages=find_packages(include=["decaf2many", "decaf2many.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/adsharma/decaf2many",
    version="0.1.0",
    zip_safe=False,
)
