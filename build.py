import os
import glob

file_top = open('index_top.html', 'r')
top_html = file_top.read()
file_top.close()

file_bottom = open('index_bottom.html', 'r')
bottom_html = file_bottom.read()
file_bottom.close()

file_build = open('index.html', 'w')
file_build.write(top_html)
for folder in glob.glob('*/'):
    folder_class = folder.replace('_', '-')
    for file in glob.glob(folder+'*.docx'):
        name = file.split('\\')[1].split('.')[0]
        if name[0] == '_':
            continue
        file_build.write(f'        <li class="recipe {folder_class}"><a>{name}</a></li>\n')
        # print(folder, name)
file_build.write(bottom_html)
file_build.close()
