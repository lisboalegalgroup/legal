import os
import re

css_file = 'css/style.css'
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. Update CSS
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace variables
css_content = re.sub(r'--primary-blue:\s*#[0-9a-fA-F]+;', '--primary-blue: #0D1B2A;', css_content) # Navy
css_content = re.sub(r'--dark-bg:\s*#[0-9a-fA-F]+;', '--dark-bg: #0D1B2A;', css_content)
css_content = re.sub(r'--accent-gold:\s*#[0-9a-fA-F]+;', '--accent-gold: #B8933F;', css_content) # Gold
css_content = re.sub(r'--accent-gold-hover:\s*#[0-9a-fA-F]+;', '--accent-gold-hover: #D4AE6A;', css_content) # Gold Light
css_content = re.sub(r'--text-dark:\s*#[0-9a-fA-F]+;', '--text-dark: #4A5568;', css_content) # Slate
css_content = re.sub(r'--bg-light:\s*#[0-9a-fA-F]+;', '--bg-light: #F5F0E8;', css_content) # Cream

# Replace generic Golos Text with Montserrat
css_content = re.sub(r"font-family:\s*'Golos Text',\s*sans-serif;", "font-family: 'Montserrat', sans-serif;", css_content)

# Update Headers to Cormorant Garamond
# Using regex to target the h1, h2, h3, h4 block
css_content = re.sub(
    r'(h1,\s*h2,\s*h3,\s*h4\s*\{\s*)font-family:\s*\'Montserrat\',\s*sans-serif;',
    r"\1font-family: 'Cormorant Garamond', serif;",
    css_content
)

# Also ensure .section-title h2 uses Cormorant
if ".section-title h2 {" in css_content and "font-family: 'Cormorant Garamond'" not in css_content:
    css_content = re.sub(
        r'(\.section-title h2\s*\{)',
        r"\1\n    font-family: 'Cormorant Garamond', serif;",
        css_content
    )

# Add Tenor Sans to .btn and uppercase elements if not present
if ".btn {" in css_content and "font-family: 'Tenor Sans'" not in css_content:
    css_content = re.sub(
        r'(\.btn\s*\{)',
        r"\1\n    font-family: 'Tenor Sans', sans-serif;",
        css_content
    )

if ".profile-role {" in css_content and "font-family: 'Tenor Sans'" not in css_content:
    css_content = re.sub(
        r'(\.profile-role\s*\{)',
        r"\1\n    font-family: 'Tenor Sans', sans-serif;",
        css_content
    )

# Ensure body uses the new cream background
if "background-color: var(--bg-light);" not in css_content:
    # Look for html, body block
    css_content = re.sub(
        r'(html,\s*body\s*\{[^}]*)',
        r'\1\n            background-color: var(--bg-light);',
        css_content
    )

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update HTML files
# We will match the old Google Fonts link which contains Golos+Text or Golos Text
# and replace it with the new fonts.

new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Tenor+Sans&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'
old_font_regex = re.compile(r'<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=Golos\+Text[^>]*>', re.IGNORECASE)

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file has the old link
    if old_font_regex.search(content):
        content = old_font_regex.sub(new_font_link, content)
    elif "Cormorant+Garamond" not in content:
        # If it doesn't have Golos but also doesn't have the new fonts, insert before </head>
        content = content.replace("</head>", f"    {new_font_link}\n</head>")

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied typography and color update to CSS and all HTML files.")
