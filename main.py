from PIL import Image
from PIL.ExifTags import TAGS
import urllib.request


def load_image(url, filename):
    """Saves and returns a picture from a url."""
    urllib.request.urlretrieve(url, filename)
    im = Image.open(filename)
    return im


url = "http://vyuka.ookami.cz/@CVUT_2015+16-LS_BI-PYT/pix/IMG_0192.original.JPG"
filename = "1.jpg"

#im = load_image(url, filename)
im = Image.open("1.jpg")
im.show()
#w, h = im.size
#im.crop((0, 0, w/2, h)).show()



