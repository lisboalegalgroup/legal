import os
import re

css_file = 'css/style.css'
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. Update CSS
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace variables back to original
css_content = re.sub(r'--primary-blue:\s*#[0-9a-fA-F]+;', '--primary-blue: #05142a;', css_content)
css_content = re.sub(r'--dark-bg:\s*#[0-9a-fA-F]+;', '--dark-bg: #030a15;', css_content)
css_content = re.sub(r'--accent-gold:\s*#[0-9a-fA-F]+;', '--accent-gold: #d4af37;', css_content)
css_content = re.sub(r'--accent-gold-hover:\s*#[0-9a-fA-F]+;', '--accent-gold-hover: #b5952f;', css_content)
css_content = re.sub(r'--text-dark:\s*#[0-9a-fA-F]+;', '--text-dark: #1F2937;', css_content)
css_content = re.sub(r'--bg-light:\s*#[0-9a-fA-F]+;', '--bg-light: #FAFAFA;', css_content)

# Replace fonts back to Golos Text
css_content = re.sub(r"font-family:\s*'Montserrat',\s*sans-serif;", "font-family: 'Golos Text', sans-serif;", css_content)
css_content = re.sub(r"font-family:\s*'Cormorant Garamond',\s*serif;", "font-family: 'Golos Text', sans-serif;", css_content)

# Remove Tenor Sans
css_content = re.sub(r"\s*font-family:\s*'Tenor Sans',\s*sans-serif;", "", css_content)

# Remove background-color: var(--bg-light); from html, body
css_content = re.sub(r"(\s*background-color:\s*var\(--bg-light\);\s*\/\*\s*Cream background\s*\*\/)", "", css_content)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update HTML files
old_font_link = '<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700&display=swap" rel="stylesheet">'
new_font_regex = re.compile(r'<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=Cormorant\+Garamond[^>]*>', re.IGNORECASE)

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if new_font_regex.search(content):
        content = new_font_regex.sub(old_font_link, content)
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Reverted typography and color updates.")
