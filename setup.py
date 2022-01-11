from setuptools import setup, find_packages
import os 
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Generate random mutations of an image for an NFT collection'

# Setting up
setup(
    name="generate_nft",
    version=VERSION,
    author="Prasad Mecheri Chandravihar",
    author_email="<prasadmecheri@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['Pillow==9.0.0'],
    license_files = ('LICENSE.txt',),
    keywords=['python', 'NFT', 'Generative-art', 'collections', 'NFTS', 'random image'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

