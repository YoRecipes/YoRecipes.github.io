# Yo! Recipes!

Website with all recipies of Yollaine.

https://yorecipes.github.io/

## How to add a recipe:

1. Add the `.docx` file in the appropriate folder (`DOCX/desserts/`, `DOCX/ice_creams/`, `DOCX/main_courses/`, or `DOCX/starters/`)
2. Make sure the needed extensions are installed.
3. Run the `build.py` script. This will automatially translate the document to other languages, convert to PDF/PNG/HTML, and index to the main page.

## Extensions needed:

```bash
pip install docx2pdf
pip install pdf2image
pip install Unidecode
pip install deep_translator
pip install python-docx
```
