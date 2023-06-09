'''
Author: Rushab Shah
Code: parser.py
Purpose: To read PDF files and extract text out of it and return it in a structured format
'''
import glob
import os
import json
import re
from pdfminer.high_level import extract_text
from extract import extract_features
import cloudinary.uploader
from PyPDF2 import PdfReader,PdfWriter
from pdf2image import convert_from_path

cloudinary.config( 
  cloud_name = "dajjzo6cq",
  api_key = "351438585191861",
  api_secret = "cfR4pj1M3E-BOV1KFsrQjGiwqAk"
)

RAWDATA_PATH = "../datasources/raw-data"
PROCESSED_DATA_PATH = "../datasources/processed-data/"
PROCESSED_FILE_NAME = "preprocessed-data.json"
SNAPSHOT_LOCATION = "../output/snapshots/"
CHUNK_SIZE = 5000
PDF_TEXT_MAP = {}

def parse(filepaths):
    """
    Parse a PDF file and return text in structured format
    """
    print("Reading Input Files ...")
    for filepath in filepaths:
        # For each research paper
        upload_screenshot(filepath)
        data = extract_text(filepath)
        data = data.strip().replace('\n', '\\n').replace('"', '\\"')
        break_into_chunks(data,filepath)
    print("Read Finished. Saving preprocessed data")
    save_to_txt()
    print("Starting the feature extraction")
    extract_features(PROCESSED_DATA_PATH+PROCESSED_FILE_NAME)

def upload_screenshot(filepath):
    """
    This method is responsible for uploading the snapshot of research papers to cloudinary
    """
    filename = get_filename_from_path(filepath)
    url_filename = make_url_friendly(filename)
    capture_screenshot(filepath,SNAPSHOT_LOCATION+url_filename+".jpg")
    # print("Uploading screenshot for "+filename)
    cloudinary.uploader.upload(SNAPSHOT_LOCATION+url_filename+".jpg", public_id = url_filename)

def make_url_friendly(filename):
    """
    This method is responsible for making a filename URL friendly
    """
    # Convert to lowercase
    filename = filename.lower()

    # Remove leading and trailing whitespace
    filename = filename.strip()

    # Replace spaces with underscores
    filename = filename.replace(" ", "_")

    # Remove special characters
    filename = re.sub(r'\W+', '', filename)
    return filename


def capture_screenshot(pdf_path,output_path):
    """
    This method is responsible for capturing the screenshot of the first page of a PDF and saving it
    """
    # print("Capturing screenshot for " + str(pdf_path))

    # Open the PDF file
    with open(pdf_path, "rb") as file:
        pdf = PdfReader(file)
        # Create a new PDF writer
        writer = PdfWriter()

        # If the file has more than one page, remove the rest
        if len(pdf.pages) > 1:
            writer.add_page(pdf.pages[0])

        # Write the resulting PDF to a temporary file
        temp_path = "temp.pdf"
        with open(temp_path, "wb") as temp_file:
            writer.write(temp_file)

        # Convert the first page to an image
        images = convert_from_path(temp_path)

        # Save the first page image to file
        images[0].save(output_path, 'JPEG')

        # Delete the temporary PDF file
        os.remove(temp_path)

def break_into_chunks(pdf_string, filepath):
    """
    Breaking the pdf string into more manageable chunks
    """
    chunks = [pdf_string[i:i+CHUNK_SIZE] for i in range(0, len(pdf_string), CHUNK_SIZE)]
    ## Associate each pdf with its text chunk
    PDF_TEXT_MAP[get_filename_from_path(filepath)] = chunks


def get_filename_from_path(filepath):
    """
    Method to extract a filename from its path. Resulting file name is without its extension
    """
    filename = os.path.splitext(os.path.basename(filepath))[0]
    return filename

def save_to_txt():
    """
    Save the parsed pdf text into a local text file
    """
    with open(PROCESSED_DATA_PATH+PROCESSED_FILE_NAME,'w') as file_object:
        file_object.write(json.dumps(PDF_TEXT_MAP))
    print("Preprocessed data stored")

def get_paper_list():
    """
    This method is responsible to get a list of PDF file paths to be processed
    """
    pdf_files = glob.glob(RAWDATA_PATH + '/*.pdf')
    return pdf_files

def main():
    """
    Main method. Serves as Entry point
    """
    # Get List of Files
    # Pass it to parse
    parse(get_paper_list())


if __name__ == "__main__":
    main()
