import glob
import os
import time

# --------------------------------------------------
# Get the last modified timestamp

last_modified_timestamp = 0
f = open('last_update_timestamp.txt', 'r')
last_modified_timestamp = int(f.read().strip())
f.close()
print(last_modified_timestamp)

# --------------------------------------------------
# Convert DOCX to PDF

# Using the library "docx2pdf" (https://github.com/AlJohri/docx2pdf)
# 
# `pip install docx2pdf`
from docx2pdf import convert

# Convert example:
# ```python
# in_file = "DOCX/starters/Canneles Pesto Parmesan.docx"
# out_file = "PDF/starters/Canneles Pesto Parmesan.pdf"
# 
# convert(in_file, out_file)
# ```

# convert("DOCX/desserts/Banana Bread.docx", "PDF/desserts/Banana Bread.pdf")

for folder in glob.glob('DOCX\\*\\'):
    sub_folder = folder.split('\\')[1]
    for file in glob.glob(folder+'*.docx'):
        if '\\_' in file:
            continue
        new_file = file.replace('.docx', '.pdf').replace('DOCX', 'PDF')
        modified_time = os.path.getmtime(file)
        if modified_time > last_modified_timestamp:
            print(file)
            print(new_file)
            convert(file, new_file)

print()

# --------------------------------------------------
# Convert PDF to PNG

# Using the library "pdf2image" (https://pypi.org/project/pdf2image/)
# 
# `pip install pdf2image`

from pdf2image import convert_from_path

# Convert example:
# ```python
# images = convert_from_path('PDF/desserts/Banana Bread.pdf')
# # images is a list of PIL images (one per page)
# for i,image in enumerate(images):
#     image.save(f'PNG/desserts/Banana Bread{i}.pdf')
# ```

# images = convert_from_path('PDF/desserts/Banana Bread.pdf')
# images[0].save('PNG/desserts/Banana Bread.png', 'PNG')

for folder in glob.glob('PDF\\*\\'):
    sub_folder = folder.split('\\')[1]
    for file in glob.glob(folder+'*.pdf'):
        if '\\_' in file:
            continue
        new_file = file.replace('.pdf', '.png').replace('PDF', 'PNG')
        modified_time = os.path.getmtime(file)
        if modified_time > last_modified_timestamp:
            print(file)
            print(new_file)
            images = convert_from_path(file)
            images[0].save(new_file, 'PNG')


print()

# --------------------------------------------------
# Convert PNG to HTML

for folder in glob.glob('PNG\\*\\'):
    sub_folder = folder.split('\\')[1]
    for file in glob.glob(folder+'*.png'):
        if '\\_' in file:
            continue
        recipe_name = file.split('\\')[-1].replace('.png', '')
        new_file = file.replace('.png', '.html').replace('PNG', 'HTML')
        modified_time = os.path.getmtime(file)
        if modified_time > last_modified_timestamp:
            print(file)
            print(new_file)
            file_png = file.replace('\\', '/')
            file_pdf = file.replace('PNG', 'PDF').replace('.png', '.pdf').replace('\\', '/')
            file_docx = file.replace('PNG', 'DOCX').replace('.png', '.docx').replace('\\', '/')
            txt = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yo! Recipes!</title>
    <style>
        @font-face {
            font-family: monotypeCorsiva;
            src: url(../../monotype-corsiva.ttf);
        }

        #back-button {
            display: inline-block;
            padding: 0.25em 0.5em;
            margin: 0.1em;
            background-color: #ccc;
            border-radius: 0.5em;
            cursor: pointer;
            user-select: none;
            font-weight: bold;
            font-size: 1.1em;
            text-decoration: none;
            user-select: none;
        }

        body {
            display: flex;
            align-items: center;
            flex-direction: column;
            margin: 0;
            padding: 0;
            font-family: monotypeCorsiva;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        .icon {
            width: 40px;
            height: 40px;
            margin: 0 5px;
        }

        .recipe-image {
            width: 99%;
            max-width: 750px;
            margin: 1em 10px;
            box-shadow: #666 0 0 10px;
        }
    </style>
</head>

<body>
    <!-- <a href="../../index.html" id="back-button">← Back  ↺</a> -->
    <a href="../../index.html" id="back-button">Back to List</a>
    <h1>Yo! Recipes!</h1>
    <div>
        <a href="../../''' + file_png + '''"><img src="../../logo_png.svg" alt="png file" class="icon"></a>
        <a href="../../''' + file_pdf + '''"><img src="../../logo_pdf.svg" alt="pdf file" class="icon"></a>
        <a href="../../''' + file_docx+ '''"><img src="../../logo_docx.svg" alt="docx file" class="icon"></a>
    </div>
    <img src="../../''' + file.replace('\\', '/') + '''" alt="''' + recipe_name + ''' Recipe" class="recipe-image">

</body>


</html>'''
            with open(new_file, 'w') as f:
                f.write(txt)

# --------------------------------------------------
# Save the last modified timestamp

f = open('last_update_timestamp.txt', 'w')
f.write(str(int(time.time())))
f.close()

# --------------------------------------------------
# Build the index.html

from unidecode import unidecode

file_top = open('index_top.html', 'r')
top_html = file_top.read()
file_top.close()

file_bottom = open('index_bottom.html', 'r')
bottom_html = file_bottom.read()
file_bottom.close()

file_build = open('index.html', 'w')
file_build.write(top_html + '\n')

lines = []
for folder in glob.glob('HTML\\*\\'):
    folder_class = folder.replace('_', '-').replace('\\', '').replace('HTML', '')
    for file in glob.glob(folder+'*.html'):
        name = file.split('\\')[2].split('.')[0]
        redirect = file.replace("\\", "/")
        if name[0] == '_':
            continue
        lines.append( (unidecode(name), f'        <li class="recipe {folder_class}"><a href="{redirect}">{name}</a></li>\n') )

lines.sort()
for line in lines:
    file_build.write(line[1])

file_build.write(bottom_html)
file_build.close()
