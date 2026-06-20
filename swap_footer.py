import glob, codecs
import re

files = glob.glob('*.html')
pattern = re.compile(r'(<div class="footer-bottom">\s*)<div class="footer-empty"></div>(.*?)\s*<div class="footer-social">(.*?)</div>\s*</div>', re.DOTALL)

def replacer(match):
    start_tag = match.group(1)
    middle = match.group(2)
    social_inner = match.group(3)
    
    new_html = start_tag + '                <div class="footer-social">' + social_inner + '</div>\n' + middle + '\n                <div class="footer-empty"></div>\n            </div>'
    return new_html

for f in files:
    content = codecs.open(f, 'r', 'utf-8').read()
    new_content = pattern.sub(replacer, content)
    
    if content != new_content:
        codecs.open(f, 'w', 'utf-8').write(new_content)
        print(f'Updated {f}')
