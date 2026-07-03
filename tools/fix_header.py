import os
import re

files = ['daniel-espinoza.html', 'karol-carvajal.html', 'gustavo-san-andres.html']

script_regex = re.compile(r'<script>\s*// Header Scroll Effect.*?window\.addEventListener\(\'scroll\'.*?\}\);\s*</script>', re.DOTALL)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change <header> to <header class="scrolled">
    content = content.replace('<header>', '<header class="scrolled">')
    
    # Just in case it was already replaced
    content = content.replace('<header class="scrolled" class="scrolled">', '<header class="scrolled">')

    # Remove the script
    content = script_regex.sub('', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed headers in profile pages.")
