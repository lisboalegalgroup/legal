import codecs
import re

file_path = 'index.html'
content = codecs.open(file_path, 'r', 'utf-8').read()

# Replace fonts
content = re.sub(r'<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=Golos\+Text[^>]*>', '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Tenor+Sans&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">', content)

# Replace text
content = content.replace("Lisboa Legal Group", "San Andrés Legal Group")
content = content.replace("Lisboa Legal", "San Andrés Legal")
content = content.replace("Lisboa", "San Andrés")
content = content.replace("LISBOA", "SAN ANDRÉS")
content = content.replace("lisboalegalgroup@gmail.com", "info@slggroup.ec")

# Replace Logo
logoHtml = """<div class="slg-lockup">
    <div class="slg-letters">SLG</div>
    <div class="slg-rule-wrap">
        <div class="slg-rule"></div><div class="slg-dot"></div><div class="slg-rule"></div>
    </div>
    <div class="slg-firm">San Andrés Legal Group</div>
</div>"""

content = re.sub(r'<img[^>]*src="logo-full\.png"[^>]*>', logoHtml, content)
content = re.sub(r'<img[^>]*src="ChatGPT Image 26 ago 2025, 14_11_32\.png"[^>]*>', logoHtml, content)

codecs.open(file_path, 'w', 'utf-8').write(content)
