============================================ README =============================================
The two scripts, insert_metadata.py and extract_metadata.py, enable you to cut a stereoscopic 
.jpg image in half, add specific metadata and save in a new file. The specific metadata is a
.png image and a .txt document.

-------------------------------------- INSERT_METADATA.PY ---------------------------------------
Cuts a stereoscopic image vertically in half, adds the metadata and saves in a separate file.

 - usage:
	$ python insert_metadata.py arg1 arg2 arg3
 - arguments:
	arg1: source stereoscopic .jpg file
	arg2: .png metadata file
	arg3: .txt metadata file
 - output: a RESULT .jpg file
 - note: the script will crash if you use a different number or order of arguments
 - note: do NOT rename the RESULT .jpg file, otherwise extract_metadata.py will not work
 
 -------------------------------------- EXTRACT_METADATA.PY -------------------------------------
Extracts back the metadata and cut-off image from the RESULT .jpg created by insert_metadata.py.
 - usage:
	$ python extract_metadata.py arg1
 - arguments:
	arg1: RESULT .jpg file created by the insert_metadata.py script.
 - output:
	ORIGINAL_IMAGE.jpg - left half of the original image
	META_IMAGE.png - .png metadata file
	META_TEXT.txt - .txt metadata file
 - note: the script will crash if you use a different number of arguments
 - note: the script will crash if the RESULT file is renamed
 
-------------------------- EXAMPLE: HOW TO USE WITH PROVIDED SAMPLE FILES -----------------------
$ python insert_metadata.py source_image.jpg image_metadata.png text_metadata.txt.
		- creates RESULT image, in this case named "RESULT-247696-496576-502804.jpg"
$ python extract_metadata.py RESULT-247696-496576-502804.jpg
		- extracts the metadata back from the RESULT file.
=================================================================================================