# Yo! Recipes!

Website with all recipies of Yollaine.

https://yorecipes.github.io/

## How to add a recipe:

1. Add the `.docx` file in the appropriate folder (`DOCX/desserts/`, `DOCX/ice_creams/`, `DOCX/main_courses/`, or `DOCX/starters/`)
2. Make sure the needed extensions are installed.
3. Run the `build_all.py` script. This will automatially convert to PDF, PNG, HTML, and index to the main page.

## Extensions needed:

TL;DR:

```bash
pip install docx2pdf
pip install pdf2image
pip install Unidecode
```

### Convert DOCX to PDF

Using the library "docx2pdf" (https://github.com/AlJohri/docx2pdf); run `pip install docx2pdf` to install.

### Convert PDF to PNG

Using the library "pdf2image" (https://pypi.org/project/pdf2image/); run `pip install pdf2image` to install.

### Indexing all recipies

Using the library Unidecode to ignore accents (https://pypi.org/project/Unidecode/); run `pip install Unidecode` to install.
