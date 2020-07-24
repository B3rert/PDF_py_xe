#https://iq.opengenus.org/pdf_to_image_in_python/

import pdf2image
from PIL import Image
import time
import sys

#DECLARE CONSTANTS
PDF_PATH = sys.argv[1]
DPI = 200
OUTPUT_FOLDER = sys.argv[2]
FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 1
USERPWD = None
USE_CROPBOX = False
STRICT = False

def pdftopil(PDF_PATH,OUTPUT_FOLDER):
    start_time = time.time()
    pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
    print ("Time taken : " + str(time.time() - start_time))
    return pil_images
    
def save_images(pil_images):
    index = 1
    for image in pil_images:
        image.save("page_" + str(index) + ".jpg")
        index += 1

if __name__ == "__main__":
    pil_images = pdftopil(PDF_PATH,OUTPUT_FOLDER)
    save_images(pil_images)