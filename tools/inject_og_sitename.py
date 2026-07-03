import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<head>' not in content.lower():
        return

    # Check if we already have the custom site_name meta tag to avoid duplicating
    if 'og:site_name' in content:
        print(f"Skipping {filepath}: og:site_name already present")
        return

    # Find the title tag
    title_match = re.search(r'<title>.*?</title>', content, flags=re.IGNORECASE | re.DOTALL)
    if title_match:
         # Insert right after title
         insertion_point = title_match.end()
         og_tag = '\n    <meta property="og:site_name" content="Lisboa Legal Group">'
         new_content = content[:insertion_point] + og_tag + content[insertion_point:]
    else:
         # Fallback to </head>
         og_tag = '    <meta property="og:site_name" content="Lisboa Legal Group">\n'
         new_content = re.sub(r'(</head>)', rf'{og_tag}\1', content, count=1, flags=re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

def main():
    directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file in html_files:
        process_file(file)

if __name__ == '__main__':
    main()
