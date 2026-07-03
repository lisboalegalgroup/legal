import os
import glob
import re

html_files = glob.glob('*.html')

replacements = {
    'Abg.%20Daniel.webp': 'Daniel%20Modelo.webp',
    'Abg.%20Daniel.png': 'Daniel%20Modelo.png',
}

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)

    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

print("Done")
