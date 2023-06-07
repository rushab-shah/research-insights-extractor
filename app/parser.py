'''
Author: Rushab Shah
Code: parser.py
Purpose: To read PDF files and extract text out of it and return it in a structured format
'''
from pdfminer.high_level import extract_text
from extract import extract_features

RAWDATA_PATH = "../datasources/raw-data"
PROCESSED_DATA_PATH = "../datasources/processed-data"
CHUNK_SIZE = 6000
# SECTIONS = ["ABSTRACT", "INTRODUCTION", "METHODOLOGY", "RESULTS", "DISCUSSION", "CONCLUSIONS"]

def parse(filename):
    """
    Parse a PDF file and return text in structured format
    """
    print("Parsing...")
    data = extract_text(RAWDATA_PATH+"/"+filename)
    data = data.strip().replace('\n', '\\n').replace('"', '\\"')
    break_into_chunks(data)

# def extract_sections_from_text(pdf_string):
#     """
#     TODO
#     """
#     print("Extracting sections")
#     save_to_txt()

def break_into_chunks(pdf_string):
    """
    Breaking the pdf string into more manageable chunks
    """
    chunks = [pdf_string[i:i+CHUNK_SIZE] for i in range(0, len(pdf_string), CHUNK_SIZE)]
    save_to_txt(chunks)

def save_to_txt(chunks):
    """
    Save the parsed pdf text into a local text file
    """
    print("Transferring data to txt")
    count = 0
    with open(PROCESSED_DATA_PATH+"/"+"op.txt",'w') as file_object:
        for chunk in chunks:
            count+=1
            file_object.write("Chunk "+str(count)+"\n\n")
            file_object.write(chunk)
            file_object.write("\n\n")
    extract_features(chunks)


def main():
    """
    Main method
    """
    parse("11606_2022_Article_7414.pdf")


if __name__ == "__main__":
    main()
