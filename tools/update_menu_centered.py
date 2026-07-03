import re
import os
import glob

directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
os.chdir(directory)

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '.menu-toggle' in content:
        if 'margin-left: auto;' not in content:
            new_content = re.sub(
                r'(\.menu-toggle\s*\{\s*display:\s*block;[^\}]*?)(?=\s*\})',
                r'\1\n                margin-left: auto;',
                content,
                count=1 # only the first one
            )
            
            if new_content != content:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file}")
            else:
                print(f"Regex didn't match anything in {file} even though .menu-toggle is there.")
        else:
            print(f"Already fixed {file}")
    else:
        print(f"No .menu-toggle found in {file}")
