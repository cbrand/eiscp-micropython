import os
import sys
from typing import List

from setuptools import find_namespace_packages, setup

import sdist_upip

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)
EGG_NAME = "eiscp-micropython"


def list_packages(source_directory: str = ".") -> List[str]:
    packages = list(find_namespace_packages(source_directory, exclude="venv"))
    return packages


version = "0.9.8"
requirements = []
test_requirements = ["twine", "adafruit-ampy>=1.0.0"]

if os.path.isfile("README.md"):
    with open("README.md", "r") as handle:
        long_description = handle.read()
else:
    long_description = ""


setup(
    name=EGG_NAME,
    version=version,
    python_requires=">={}.{}".format(*REQUIRED_PYTHON),
    url="https://github.com/cbrand/eiscp-micropython",
    author="Christoph Brand",
    author_email="ch.brand@gmail.com",
    description="Micropython packages for the Onkyo EISCP protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=list_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia",
        "License :: OSI Approved :: MIT License",
    ],
    extras_require={},
    project_urls={"GitHub": "https://github.com/cbrand/eiscp-micropython"},
    cmdclass={"sdist": sdist_upip.sdist},
)
