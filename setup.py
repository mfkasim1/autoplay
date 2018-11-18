import os
from setuptools import setup, find_packages
from autoplay.version import get_version

setup(
    name='autoplay',
    version=get_version(),
    description='A library to execute functions when some specified '\
                'changes in file system happens',
    url='https://github.com/mfkasim91/autoplay',
    author='mfkasim91',
    author_email='firman.kasim@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires=">=2.7",
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 2.7"
    ],
    keywords="automation",
    zip_safe=False
)
