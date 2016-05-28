"""extract_metadata.py
Takes the RESULT JPG file generated using insert_metadata.py and extracts PNG and TXT metadata from it. Saves the
metadata and the JPG image in separate files.

Usage:
    extract_metadata.py <RESULT JPG image>
"""


import sys
import os

sizes = list(map(int, (os.path.splitext(sys.argv[1])[0]).split(sep="-")[1:4]))  # list of byte positions for parsing
filename = sys.argv[1]

with open(filename, "rb") as f:
    a = f.read()

original_image = a[0:sizes[0]]                                                  # extracts the original image
meta_image = a[sizes[0]:sizes[1]]                                               # extracts the .png metadata
meta_text = a[sizes[1]:sizes[2]]                                                # extracts the .txt metadata

with open("ORIGINAL_FILE.jpg", "wb") as f:                                      # saves the original image
    f.write(original_image)

with open("META_IMAGE.png", "wb") as f:                                         # saves the .png metadata
    f.write(meta_image)

with open("META_TEXT.txt", "wb") as f:                                          # saves the .txt metadata
    f.write(meta_text)
