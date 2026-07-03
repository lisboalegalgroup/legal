import os
import re

css_file = 'css/style.css'
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'san-andres-legal-brand(1).html']

# 1. Update CSS
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace variables
css_content = re.sub(r'--primary-blue:\s*#[0-9a-fA-F]+;', '--primary-blue: #0D1B2A;', css_content) # Navy
css_content = re.sub(r'--dark-bg:\s*#[0-9a-fA-F]+;', '--dark-bg: #0D1B2A;', css_content)
css_content = re.sub(r'--accent-gold:\s*#[0-9a-fA-F]+;', '--accent-gold: #B8933F;', css_content) # Gold
css_content = re.sub(r'--accent-gold-hover:\s*#[0-9a-fA-F]+;', '--accent-gold-hover: #D4AE6A;', css_content) # Gold Light

# Replace fonts
css_content = re.sub(r"font-family:\s*'Golos Text',\s*sans-serif;", "font-family: 'Montserrat', sans-serif;", css_content)
css_content = re.sub(r"h1,\s*h2,\s*h3,\s*h4\s*\{\s*font-family:\s*'Golos Text',\s*sans-serif;", "h1,\n        h2,\n        h3,\n        h4 {\n            font-family: 'Cormorant Garamond', serif;", css_content)

# Add logo CSS
logo_css = """
/* --- SAN ANDRES BRAND LOGO --- */
.slg-lockup { display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 5px 0; }
.slg-letters { font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 300; line-height: 1; letter-spacing: 0.18em; color: var(--accent-gold); margin-right: -0.18em; }
.slg-rule-wrap { display: flex; align-items: center; gap: 6px; width: 100%; justify-content: center; }
.slg-rule { width: 40px; height: 1px; background: rgba(184,147,63,0.4); }
.slg-dot { width: 3px; height: 3px; border-radius: 50%; background: var(--accent-gold); }
.slg-firm { font-family: 'Tenor Sans', sans-serif; font-size: 8px; letter-spacing: 0.3em; text-transform: uppercase; color: var(--primary-blue); white-space: nowrap; }

header.scrolled .slg-firm { color: var(--primary-blue); }
.footer-brand .slg-firm { color: var(--white); }
.footer-brand .slg-rule { background: rgba(255,255,255,0.4); }
"""
if "SAN ANDRES BRAND LOGO" not in css_content:
    css_content += logo_css

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update HTML files
old_font_link = r'<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=Golos\+Text[^>]*>'
new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Tenor+Sans&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'

logo_html = """<div class="slg-lockup">
    <div class="slg-letters">SLG</div>
    <div class="slg-rule-wrap">
        <div class="slg-rule"></div><div class="slg-dot"></div><div class="slg-rule"></div>
    </div>
    <div class="slg-firm">San Andrés Legal Group</div>
</div>"""

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace fonts
    content = re.sub(old_font_link, new_font_link, content)
    
    # Replace texts
    content = content.replace("Lisboa Legal Group", "San Andrés Legal Group")
    content = content.replace("Lisboa Legal", "San Andrés Legal")
    content = content.replace("Lisboa", "San Andrés")
    content = content.replace("LISBOA", "SAN ANDRÉS")
    content = content.replace("lisboalegalgroup@gmail.com", "info@slggroup.ec")
    
    # Replace logo image
    content = re.sub(r'<img[^>]*src="logo-full\.png"[^>]*>', logo_html, content)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied brand update to CSS and all HTML files.")
