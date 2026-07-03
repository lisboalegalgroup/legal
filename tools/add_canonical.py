import glob
import re

html_files = glob.glob('*.html')
base_url = 'https://lisboalegalgroup.github.io/legal/'

for file in html_files:
    if file.startswith('google'):
        continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="canonical"' in content:
        print(f"Skipping {file}, canonical already exists.")
        continue
    
    if file == 'index.html':
        url = base_url
    else:
        url = f"{base_url}{file}"
    
    canonical_tag = f'\n    <link rel="canonical" href="{url}" />'
    
    # Insert after <head>
    # Handle possible attributes on <head> just in case, though usually it's just <head>
    # Try looking for <head> and inserting right after it.
    new_content, count = re.subn(r'(<head[^>]*>)', r'\1' + canonical_tag, content, count=1, flags=re.IGNORECASE)
    
    if count == 0:
        print(f"Warning: Could not find <head> in {file}")
    else:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file} -> {url}")

print("Done.")
