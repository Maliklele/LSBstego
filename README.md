# LSBstego - COE426 Project

Least Significant Bit (LSB) Steganography.

In this technique we will hide text data inside of an image of a fixed size, and to achieve this we will manipulate the least significant bits of the pixels data of an image to our favor using [Python](https://www.python.org/downloads/release/python-3100/)

## Usage
###### Dependancies
- [Pillow](https://pillow.readthedocs.io/en/stable/)

###### Encoding message inside of an image

1. use the [LSB_encrypt.py](https://github.com/Maliklele/LSBstego/blob/master/LSB_encrypt.py) file
2. Make sure to specify the paths for the image, output path, text file which includes the message
3. Run the application


###### Decoding message inside of an image

1. use the [LSB_decrypt.py](https://github.com/Maliklele/LSBstego/blob/master/LSB_decrypt.py) file
2. Make sure to specify the path for the image, and the output text to be save (it will also be previewd in the console)
