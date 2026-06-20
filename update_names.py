import os
import glob
import re

html_files = glob.glob('index*.html')

partners = [
    {"img": "Daniel Modelo.webp", "name": "Daniel Espinoza"},
    {"img": "Nueva foto karo.webp", "name": "Karol Carvajal"},
    {"img": "gustavo.webp", "name": "Gustavo San Andrés"}
]

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = content
    
    for partner in partners:
        pattern = re.compile(rf'(<img[^>]*src="{partner["img"]}"[^>]*>.*?)(<p)', re.DOTALL | re.IGNORECASE)
        h3_html = f'<h3 style="font-size: 1.4rem; color: var(--primary-blue); margin-bottom: 5px; font-family: \'Golos Text\', sans-serif;">{partner["name"]}</h3>\n                    '
        
        # Check if the <h3> is already inserted
        if f'>{partner["name"]}</h3>' not in new_content:
            new_content = pattern.sub(rf'\1{h3_html}\2', new_content)

    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

print("Done")
