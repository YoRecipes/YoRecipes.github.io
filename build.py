# Using the library "docx2pdf" (https://github.com/AlJohri/docx2pdf)
# `pip install docx2pdf`
from docx2pdf import convert
# Using the library "pdf2image" (https://pypi.org/project/pdf2image/)
# `pip install pdf2image`
from pdf2image import convert_from_path
# Using the library "deep_translator" (https://pypi.org/project/deep-translator/)
# `pip install deep-translator`
from deep_translator import GoogleTranslator
# Using the library "docx" (https://python-docx.readthedocs.io/en/latest/)
# `pip install python-docx`
import docx
# Using the library "unidecode" (https://pypi.org/project/Unidecode/)
# `pip install Unidecode`
from unidecode import unidecode
# standard libraries
import json
import os

def convert_docx_to_pdf(docx_folder, pdf_folder):
    """Converts all docx files in docx_folder to pdf files in pdf_folder

    Args:
        docx_folder (folder path)
        pdf_folder (folder path)
    """
    # convert docx to pdf each file in docx_folder
    for file in os.listdir(docx_folder):
        # skip if file is a temp file
        if file[0] == '_':
            continue
        pdf_path = os.path.join(pdf_folder, file.replace('.docx', '.pdf'))
        docx_path = os.path.join(docx_folder, file)
        # convert if pdf file does not exist or docx file is modified after pdf file was modified
        if not os.path.exists(pdf_path) or os.path.getmtime(docx_path) > os.path.getmtime(pdf_path):
            convert(docx_path, pdf_path)
            print(f'Converted {docx_path} to {pdf_path}')
        else:
            print(f'Skipped conversion to PDF of {docx_path}')
    print(f'Converted {docx_folder}/* to {pdf_folder}/*')

if __name__ == "__main__":
    pass