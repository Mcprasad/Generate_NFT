from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Generate random mutations of an image for an NFT collection'

# Setting up
setup(
    name="generate_nft",
    version=VERSION,
    author="Prasad Mecheri Chandravihar",
    author_email="<prasadmecheri@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['Pillow==9.0.0'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)