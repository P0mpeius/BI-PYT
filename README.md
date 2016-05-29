# insert_metadata.py
This script enables you to cut a stereoscopic .jpg image in half, add specific metadata and save in a new file. The specific metadata is:
- a .png image
- a .txt document
 
### Installation

You need Python Imaging Library installed globally:
```sh
$ pip install pillow
```
### Usage
```sh
$ python insert_metadata.py arg1 arg2 arg3
```
### Arguments
- arg1: source stereoscopic .jpg file
- arg2: .png metadata file
- arg3: .txt metadata file

### Output
 - a RESULT .jpg file
 
### Notes
- the script will crash if you use a different number or order of arguments
- do NOT rename the RESULT .jpg file, otherwise extract_metadata.py will not work

# extract_metadata.py
Extracts back the metadata and cut-off image from the RESULT .jpg created by insert_metadata.py.
### usage:
```sh
	$ python extract_metadata.py arg1
```
### arguments:
- arg1: RESULT .jpg file created by the insert_metadata.py script.

### Output
- ORIGINAL_IMAGE.jpg - left half of the original image
- META_IMAGE.png - .png metadata file
- META_TEXT.txt - .txt metadata file
### Notes
- the script will crash if you use a different number of arguments
- the script will crash if the RESULT file is renamed
# EXAMPLE: how to use with provided sample files
```sh
$ python insert_metadata.py source_image.jpg image_metadata.png text_metadata.txt
```
This creates RESULT image, in this case named "RESULT-247696-496576-502804.jpg"
```sh
$ python extract_metadata.py RESULT-247696-496576-502804.jpg
```
This extracts the metadata back from the RESULT file.


