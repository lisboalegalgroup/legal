import os
import glob
import re

directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
for filepath in glob.glob(os.path.join(directory, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else 'Lisboa Legal Group'
    
    # Get description
    desc_match = re.search(r'<meta name="description"[\s\n]*content="([^"]*)"', content, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta content="([^"]*)"[\s\n]*name="description"', content, re.IGNORECASE)
    # also handle the case where content is multiline
    
    # Better description regex handling whitespace and multiline:
    desc_match2 = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content, re.IGNORECASE)
    if desc_match2:
        description = desc_match2.group(1)
    else:
        # some formatted like <meta name="description"\n        content="...">
        desc_match3 = re.search(r'<meta\s+name="description"[\s\r\n]+content="([^"]+)"', content, re.IGNORECASE)
        description = desc_match3.group(1) if desc_match3 else 'Estudio Jurídico en Guayaquil con experiencia en derecho penal, civil, corporativo y más.'
        # remove newlines from description
        description = description.replace('\n', ' ').replace('\r', '').replace('  ', ' ')
    
    # Get canonical url
    url_match = re.search(r'<link rel="canonical" href="([^"]+)"', content, re.IGNORECASE)
    url = url_match.group(1) if url_match else 'https://lisboalegalgroup.github.io/legal/'

    og_tags = f"""
    <!-- Open Graph Tags -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://lisboalegalgroup.github.io/legal/Abg.%20Daniel.webp">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="website">
"""

    if 'og:image' in content:
        # replace existing og:image
        content = re.sub(r'<meta property="og:image" content="[^"]*">', r'<meta property="og:image" content="https://lisboalegalgroup.github.io/legal/Abg.%20Daniel.webp">', content)
    else:
        content = re.sub(r'(</head>)', f'{og_tags}\\n\\1', content, count=1, flags=re.IGNORECASE)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated og tags in all html files.")
