import glob, re

files = glob.glob('*.html')
pattern = re.compile(r'(<div class="footer-bottom">\s*)<div class="footer-social">(.*?)</div>(.*?)\s*<div class="footer-empty"></div>\s*</div>', re.DOTALL)

def replacer(match):
    start_tag = match.group(1)
    social_inner = match.group(2)
    middle = match.group(3)
    
    new_html = start_tag + '                <div class="footer-empty"></div>' + middle + '\n                <div class="footer-social">' + social_inner + '</div>\n            </div>'
    return new_html

for f in files:
    try:
        content = open(f, 'r', encoding='utf-8').read()
        new_content = pattern.sub(replacer, content)
        
        if content != new_content:
            open(f, 'w', encoding='utf-8').write(new_content)
            print(f'Reverted {f}')
    except Exception as e:
        print(f'Error on {f}: {e}')
