============================================ README ============================================
The two scripts, insert_metadata.py and extract_metadata.py, enable you to cut a stereoscopic 
.jpg image in half, add specific metadata and save in a new file. The specific metadata is a
.png image and a .txt document.
-------------------------------------- INSERT_METADATA.PY --------------------------------------
Cuts a stereoscopic image vertically in half, adds the metadata and saves in a separate file.
 - usage:
	$ python insert_metadata.py arg1 arg2 arg3
 - arguments:
	arg1: source stereoscopic .jpg file
	arg2: .png metadata file
	arg3: .txt metadata file
 - output: a RESULT jpg file
 - note: the script will crash if you use a different number or order of arguments
-------------------------------------- EXTRACT_METADATA.PY -------------------------------------
Extracts the metadata and cut-off image from the RESULT jpg file created by insert_metadata.py.
 - usage:
	$ python extract_metadata.py arg1
 - arguments:
	arg1: RESULT .jpg file created by the insert_metadata.py script.
 - output:
	ORIGINAL_IMAGE.jpg - original image cut-off 
	META_IMAGE.png - 
	META_TEXT.txt - 
 - note: the script will crash if you use a different number or order of arguments


example usage with provided sample files:
				 python insert_metadata.py source_image.jpg image_metadata.png text_metadata.txt
------------------------------------------------------------------------------------------------