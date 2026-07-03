import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Replace absolute path /favicon.png with relative favicon.png
    content = content.replace('href="/favicon.png"', 'href="favicon.png"')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} (no changes needed)")

def main():
    directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file in html_files:
        process_file(file)

if __name__ == '__main__':
    main()
