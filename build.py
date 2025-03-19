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
import re

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

def convert_all_docx_to_pdf(docx_mega_folder, pdf_mega_folder):
    """Converts recursively all docx folders in docx_mega_folder to pdf folders in pdf_mega_folder

    Args:
        docx_mega_folder (folder path)
        pdf_mega_folder (folder path)
    """
    # convert docx to pdf each sub-folder
    for folder in os.listdir(docx_mega_folder):
        # skip if folder is a temp file
        if folder == '_':
            continue
        docx_folder_path = os.path.join(docx_mega_folder, folder)
        pdf_folder_path = os.path.join(pdf_mega_folder, folder)
        if not os.path.exists(pdf_folder_path):
            os.makedirs(pdf_folder_path)
        convert_docx_to_pdf(docx_folder_path, pdf_folder_path)
    print(f'Converted {docx_mega_folder}/* to {pdf_mega_folder}/*')

def convert_pdf_to_png(pdf_folder, png_folder):
    """Converts all pdf files in pdf_folder to png files in png_folder"

    Args:
        pdf_folder (folder path)
        png_folder (folder path)
    """
    # convert docx to pdf each file in docx_folder
    for file in os.listdir(pdf_folder):
        # skip if file is a temp file
        if file[0] == '_':
            continue
        png_path = os.path.join(png_folder, file.replace('.pdf', '.png'))
        pdf_path = os.path.join(pdf_folder, file)
        # convert if pdf file does not exist or docx file is modified
        if not os.path.exists(png_path) or os.path.getmtime(pdf_path) > os.path.getmtime(png_path):
            images = convert_from_path(pdf_path)
            image = images[0]
            image.save(png_path)
            print(f'Converted {pdf_path} to {png_path}')
        else:
            print(f'Skipped conversion to PNG of {pdf_path}')
    print(f'Converted {pdf_folder}/* to {png_folder}/*')

def convert_all_pdf_to_png(pdf_mega_folder, png_mega_folder):
    """Converts recursively all pdf folders in pdf_mega_folder to png folders in png_mega_folder"
    
    Args:
        pdf_mega_folder (folder path)
        png_mega_folder (folder path)
    """
    # convert docx to pdf each sub-folder
    for folder in os.listdir(pdf_mega_folder):
        # skip if folder is a temp file
        if folder[0] == '_':
            continue
        pdf_folder_path = os.path.join(pdf_mega_folder, folder)
        png_folder_path = os.path.join(png_mega_folder, folder)
        if not os.path.exists(png_folder_path):
            os.makedirs(png_folder_path)
        convert_pdf_to_png(pdf_folder_path, png_folder_path)
    print(f'Converted {pdf_mega_folder}/* to {png_mega_folder}/*')

def create_html(file_png, file_pdf, file_docx, file_html, file_index="index.html", skip_existing=False, title=None):
    """Creates an html file with links to the png, pdf, and docx files
    
    Args:
        file_png (file path)
        file_pdf (file path)
        file_docx (file path)
        file_html (file path)
    """
    # skip if html file already exists
    if os.path.exists(file_html) and skip_existing:
        print(f'Skipped HTML creation of {file_html}')
        return None
    # read the html template
    f = open("template.html", 'r', encoding='UTF8')
    txt = f.read()
    f.close()
    # replace the placeholders with the actual file paths
    txt = txt.replace('#*+file_pdf+*#', file_pdf)
    txt = txt.replace('#*+file_docx+*#', file_docx)
    txt = txt.replace('#*+file_png+*#', file_png)
    txt = txt.replace('#*+file_index+*#', file_index)
    if title is None:
        title = file_png.split('/')[-1].replace('.png', '') + ' Recipe'
    txt = txt.replace('#*+title+*#', title)
    # write the new html file
    f = open(file_html, 'w', encoding='UTF8')
    f.write(txt)
    f.close()
    print(f'Created {file_html}')

def create_all_html(png_mega_folder, pdf_mega_folder, docx_mega_folder, html_mega_folder, index_file="index.html", skip_existing=False):
    """Creates recursively all html files in html_mega_folder
    
    Args:
        png_mega_folder (folder path)
        pdf_mega_folder (folder path)
        docx_mega_folder (folder path)
        html_mega_folder (folder path)
        index_file (file path)
    """
    for folder in os.listdir(png_mega_folder):
        # skip if folder is a temp file
        if '\\_' in folder:
            continue
        png_folder_path = os.path.join(png_mega_folder, folder)
        pdf_folder_path = os.path.join(pdf_mega_folder, folder)
        docx_folder_path = os.path.join(docx_mega_folder, folder)
        html_folder_path = os.path.join(html_mega_folder, folder)
        if not os.path.exists(html_folder_path):
            os.makedirs(html_folder_path)
        for file in os.listdir(png_folder_path):
            # skip if file is a temp file
            if '\\_' in file:
                continue
            file_png = os.path.join(png_folder_path, file)
            file_pdf = os.path.join(pdf_folder_path, file.replace('.png', '.pdf').replace('\\', '/'))
            file_docx = os.path.join(docx_folder_path, file.replace('.png', '.docx').replace('\\', '/'))
            file_html = os.path.join(html_folder_path, file.replace('.png', '.html').replace('\\', '/'))
            # check if corresponding pdf and docx files exist
            if not os.path.exists(file_pdf):
                print(f'Error creating {file_html}: PDF file does not exist')
                continue
            if not os.path.exists(file_docx):
                print(f'Error creating {file_html}: DOCX file does not exist')
                continue
            create_html(
                file_png.replace('\\', '/'),\
                file_pdf.replace('\\', '/'), \
                file_docx.replace('\\', '/'), \
                file_html.replace('\\', '/'), \
                index_file, skip_existing
            )
        print(f'Created {html_folder_path}/*')
    print(f'Created {html_mega_folder}/*')

def translate_recipe(src, dest, translator=GoogleTranslator(source='fr', target='en'), lang='en-US'):
    """Translates a recipe from src to dest

    Args:
        src (file path)
        dest (file path)
        translator: Translator object. Defaults to GoogleTranslator(source='fr', target='en').
        lang: Language for docx spell check. Defaults to 'en-US'.
    """
    doc = docx.Document(src)
    for para in doc.paragraphs:
        para.text = translator.translate(para.text)
        print('.', end='', flush=True)
    styles_element  = doc.styles.element
    rpr_default = styles_element.xpath('./w:docDefaults/w:rPrDefault/w:rPr')[0]
    lang_default = rpr_default.xpath('w:lang')[0]
    lang_default.set(docx.oxml.shared.qn('w:val'), lang)
    doc.save(dest)
    print(dest)

def translate_recipes(src_folder, dest_folder, translator=GoogleTranslator(source='fr', target='en'), lang='en-US'):
    """Translates all recipes in src_folder to dest_folder

    Args:
        src_folder (folder path)
        dest_folder (folder path)
        translator: Translator object. Defaults to GoogleTranslator(source='fr', target='en').
        lang: Language for docx spell check. Defaults to 'en-US'.
    """
    MANUAL_TRANSLATIONS = json.load(open('manual_translations.json', 'r', encoding='UTF8'))
    for src_file_name in os.listdir(src_folder):
        # skip if file is a temp file
        if src_file_name[0] == '_':
            continue
        src = os.path.join(src_folder, src_file_name)
        src_file_name = src_file_name.replace('.docx', '')
        dest_file_name = None
        if lang in MANUAL_TRANSLATIONS and src_file_name in MANUAL_TRANSLATIONS[lang]:
            dest_file_name = MANUAL_TRANSLATIONS[lang][src_file_name]
        else:
            dest_file_name = translator.translate(src_file_name)
            MANUAL_TRANSLATIONS[lang][src_file_name] = dest_file_name
        dest = os.path.join(dest_folder, dest_file_name + '.docx')
        # translate if destination file does not exist or source file is modified
        if not os.path.exists(dest) or os.path.getmtime(src) > os.path.getmtime(dest):
            translate_recipe(src, dest, translator, lang)
        else:
            print(f'Skipped translation of {src}')
    # save MANUAL_TRANSLATIONS
    f = open('manual_translations.json', 'w', encoding='UTF8')
    json.dump(MANUAL_TRANSLATIONS, f, indent=2, ensure_ascii=True)
    f.close()
    print(f'Translated {src_folder}/* to {dest_folder}/*')

def translate_all_recipes(src_mega_folder, dest_mega_folder, translator=GoogleTranslator(source='fr', target='en'), lang='en-US'):
    """Translates recursively all recipes in src_mega_folder to dest_mega_folder

    Args:
        src_mega_folder (folder path)
        dest_mega_folder (folder path)
        translator: Translator object. Defaults to GoogleTranslator(source='fr', target='en').
        lang: Language for docx spell check. Defaults to 'en-US'.
    """
    for folder in os.listdir(src_mega_folder):
        # skip if folder is a temp file
        if folder[0] == '_':
            continue
        src_folder = os.path.join(src_mega_folder, folder)
        dest_folder = os.path.join(dest_mega_folder, folder)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        translate_recipes(src_folder, dest_folder, translator, lang)
    print(f'Translated {src_mega_folder}/* to {dest_mega_folder}/*')

def create_index(lang='fr-FR', html_mega_folder=None, index_file=None):
    """Creates an index file with links to all html files in html_mega_folder

    Args:
        lang: Language for the index file. Defaults to french.
        html_mega_folder (folder path)
        index_file (file path)
    """
    # default values
    lang_ = lang.split('-')[0]
    if html_mega_folder is None:
        if lang_ == 'fr':
            html_mega_folder = 'HTML'
        else:
            html_mega_folder = 'HTML-' + lang_
    if index_file is None:
        index_file = lang_ +'.html'
    # load manual translations
    f = open('manual_translations.json', 'r', encoding='UTF8')
    MANUAL_TRANSLATIONS = json.load(f)[lang]
    f.close()
    # top html template
    file_top = open('index_top.html', 'r', encoding='UTF8')
    top_html = file_top.read()
    file_top.close()
    # replce {{var}} in template with the actual values
    for var in re.findall(r'{{\w+}}', top_html):
        var_ = var.replace('{{', '').replace('}}', '')
        if var_ in MANUAL_TRANSLATIONS:
            top_html = top_html.replace(var, MANUAL_TRANSLATIONS[var_])
    # bottom html template
    file_bottom = open('index_bottom.html', 'r', encoding='UTF8')
    bottom_html = file_bottom.read()
    file_bottom.close()
    # create the index file
    file_build = open(index_file, 'w', encoding='UTF8')
    file_build.write(top_html + '\n')
    # li elements
    li = []
    if not os.path.exists(html_mega_folder):
        os.makedirs(html_mega_folder)
    for folder in os.listdir(html_mega_folder):
        # skip if folder is a temp file
        if folder[0] == '_':
            continue
        for file in os.listdir(os.path.join(html_mega_folder, folder)):
            # skip if file is a temp file
            if file[0] == '_':
                continue
            print(file)
            name = file.replace('.html', '')
            redirect = os.path.join(html_mega_folder, folder, file).replace("\\", "/")
            print(name, redirect)
            li.append( (unidecode(name), f'        <li class="recipe {folder.replace("_", "-")}"><a href="{redirect}">{name}</a></li>\n') )
    li.sort()
    for line in li:
        file_build.write(line[1])
    file_build.write(bottom_html)
    print(f'Created {index_file}')


if __name__ == "__main__":
    ### French
    # convert all docx to pdf
    convert_all_docx_to_pdf('DOCX', 'PDF')
    # convert all pdf to png
    convert_all_pdf_to_png('PDF', 'PNG')
    # create all html files
    create_all_html('PNG', 'PDF', 'DOCX', 'HTML', 'fr.html')
    create_index('fr-FR')
    create_index('fr-FR', index_file='index.html')
    print('Done!')
    print('\n'*3)

    ### English
    # translate all recipes to English
    translate_all_recipes('DOCX', 'DOCX-en', GoogleTranslator(source='fr', target='en'), 'en-US')
    # convert all docx to pdf
    convert_all_docx_to_pdf('DOCX-en', 'PDF-en')
    # convert all pdf to png
    convert_all_pdf_to_png('PDF-en', 'PNG-en')
    # create all html files
    create_all_html('PNG-en', 'PDF-en', 'DOCX-en', 'HTML-en', 'en.html')
    create_index('en-US')
    print('ENGLISH: Done!')
    print('\n'*3)

    create_index('sp-ES')
    print('SPANISH: Done!')
    print('\n'*3)
    
    create_index('it-IT')
    print('ITALIAN: Done!')
    print('\n'*3)
