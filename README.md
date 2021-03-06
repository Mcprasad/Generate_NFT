# Generate_NFT : Create random mutations of a picture for NFT collections
[![PyPI Latest Release](https://img.shields.io/pypi/v/generate-nft.svg)](https://pypi.org/project/generate-nft)
[![Package Status](https://img.shields.io/pypi/status/generate-nft.svg)](https://pypi.org/project/generate-nft/)
[![License](https://img.shields.io/pypi/l/generate-nft.svg)](https://github.com/Mcprasad/Generate_NFT/blob/main/LICENSE)

## What is it?

**generate-nft** is a Python package that creates multiple random mutations of a given picture without needing to feed separate layers of the image. Just provide one image and it can generate multiple variants of that image quickly. 

**Version = 0.0.4**

## Main Features
Here are just a few of the things that generate-nft does internally:

  - Split the given image into mutliple color channels - RGB, RGBA etc.. 
  - Mix and match these color channels randomly to create unique images 
  - Creates random background images to make it more unique
  - enhance the color, contrast & brightness of the image randomly 
  - Define an experiment name - the output files will be stored with that name as prefix 

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/Mcprasad/Generate_NFT

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/generate-nft/#files)

```sh
#PyPI
pip install generate-nft
```

To update the existing version of the package
```sh
#pypi
pip install -U generate-nft
```


## Installation from sources
Follow the steps given below to install the package from the source 

  - Clone the github repo 
    ```sh
    https://github.com/Mcprasad/Generate_NFT.git
    ```
  - Run setup.py 
    ```sh
    python3 setup.py sdist bdist_wheel
    ```

## How to use
```sh
from Generate_NFT import generate_art
generate_art.generate("input_image_path","output_image_directory",number_of_mutations,output_width,output_height,experiment_name)
```

An example is shown below:
```sh
from Generate_NFT import generate_art

#Program will output with the given experiment name as the prefix 
experiment_name = "mountains"
generate_art.generate("/documents/img.jpg","/documents/output/",50,1920,1920,experiment_name)
```

## License
[MIT License](https://github.com/Mcprasad/Generate_NFT/blob/main/LICENSE)

## Future Ideas

  - Ability to combine traits from multiple images 
  - Extract objects from an image and superimpose those
  - Generate meta data for each image in ERC721 standard 
  - Ability to launch the collections into a preferred blockchain; create and register contract, link metamask wallet and IPFS 











 