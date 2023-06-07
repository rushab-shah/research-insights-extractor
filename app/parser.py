'''
Author: Rushab Shah
Code: parser.py
Purpose: To read PDF files and extract text out of it and return it in a structured format
'''
import glob
import os
from pdfminer.high_level import extract_text
from extract import extract_features

RAWDATA_PATH = "../datasources/raw-data"
PROCESSED_DATA_PATH = "../datasources/processed-data/"
PROCESSED_FILE_NAME = "preprocessed-data.json"
CHUNK_SIZE = 6000
PDF_TEXT_MAP = {}

def parse(filepaths):
    """
    Parse a PDF file and return text in structured format
    """
    print("Parsing...")
    for filepath in filepaths:
        # For each research paper
        print(filepath)
        data = extract_text(filepath)
        data = data.strip().replace('\n', '\\n').replace('"', '\\"')
        break_into_chunks(data,filepath)
    print("Parsed. Now saving preprocessed data")
    save_to_txt()
    print("Now starting the extraction phase")
    extract_features(PROCESSED_DATA_PATH+PROCESSED_FILE_NAME)


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
    print(filename)
    return filename

def save_to_txt():
    """
    Save the parsed pdf text into a local text file
    """
    with open(PROCESSED_DATA_PATH+PROCESSED_FILE_NAME,'w') as file_object:
        file_object.write(PDF_TEXT_MAP)
    print("Preprocessed data stored")

def get_paper_list():
    """
    TODO
    """
    pdf_files = glob.glob(RAWDATA_PATH + '/*.pdf')
    return pdf_files

def main():
    """
    Main method
    """
    # Get List of Files
    # Pass it to parse
    parse(get_paper_list())


if __name__ == "__main__":
    main()
