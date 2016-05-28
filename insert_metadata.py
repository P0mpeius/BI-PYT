"""insert_metadata.py
Cuts an image vertically in half. Inserts PNG and TXT metadata.

Usage:
    insert_metadata.py <source JPG image> <metadata PNG image> <metadata TXT file>
"""


from PIL import Image
import os
import sys


def insert_metadata(infile, text, image):
    """
    Appends txt and png metadata to a jpg file. Saves the result in a new jpg file. The new jpg file's name is "RESULT-"
    followed by a sequence of hyphen-delimited numbers, indicating byte positions where metadata elements start or end.
    :param infile: source .jpg file path
    :param text: .txt metadata file path
    :param image: .png metadata file path
    """
    with open(infile, "rb") as f:
        a = f.read()

    with open(text, "rb", ) as f:
        b = f.read()

    with open(image, "rb") as f:
        c = f.read()

    all = a+b+c

    sizes = [len(a), len(a)+len(b), len(all)]
    filename = "RESULT"

    for i in range(len(sizes)):
        filename += "-" + str(sizes[i])
    filename += ".jpg"

    with open(filename, "wb") as f:
        f.write(all)


def crop_image(infile, outfile):
    """
    Cuts an image vertically in half. Saves the left side in a new file.
    :param infile: source image file path
    :param outfile: path where the left half will be saved
    """
    im = Image.open(infile)
    w, h = im.size
    im.crop((0, 0, w / 2, h)).save(outfile)

original_image = sys.argv[1]
meta_image = sys.argv[2]
meta_text = sys.argv[3]
temp = "TEMP.jpg"
crop_image(original_image, temp)                # cuts the source jpeg in half and saves it in a temporary file
insert_metadata(temp, meta_image, meta_text)    # takes the temp file, adds metadata to it and saves the result
os.remove(temp)                                 # deletes the temporary file

