import os
import re
import glob

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add Favicon
    if '<link rel="icon"' not in content:
        content = re.sub(
            r'(<head>.*?)(<meta)', 
            r'\1<link rel="icon" href="ChatGPT Image 26 ago 2025, 14_11_32.png" type="image/png">\n    \2', 
            content, 
            flags=re.IGNORECASE | re.DOTALL,
            count=1
        )

    # 2. Add Meta Description (Basic SEO). Extract Title to make it relevant.
    if '<meta name="description"' not in content:
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            title = title_match.group(1).replace(' | Lisboa Legal Group', '')
            desc = f'Firma de abogados de excelencia en Guayaquil, Ecuador. {title}. Asesoría corporativa y litigios de alta complejidad.'
            content = re.sub(
                r'(</title>)',
                rf'\1\n    <meta name="description" content="{desc}">',
                content,
                flags=re.IGNORECASE
            )

    # 3. Add Alt tags to images that don't have them
    # For Unsplash, just add alt="Lisboa Legal Group"
    content = re.sub(
        r'(<img(?![^>]*\balt=)[^>]*?)>', 
        r'\1 alt="Lisboa Legal Group">', 
        content,
        flags=re.IGNORECASE
    )
    # 4. Add Privacy Policy link to Footer
    if 'privacidad.html' not in content.split('<footer>')[-1]:
        content = re.sub(
            r'(<p>&copy; 2026 Lisboa Legal Group\.)(</p>)',
            r'\1 | <a href="privacidad.html" style="color: #ccc; text-decoration: underline; margin-left:10px; font-size: 0.9rem;">Políticas de Privacidad</a>\2',
            content,
            flags=re.IGNORECASE
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} HTML files.")
