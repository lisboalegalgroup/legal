import os
import re

directory = '.'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if og:site_name already exists to avoid duplication
    if 'og:site_name' not in content:
        # Insert og properties just after <meta name="viewport" ...>
        og_tags = """
    <meta property="og:site_name" content="Lisboa Legal Group">
    <meta property="og:title" content="Lisboa Legal Group | Abogados en Guayaquil, Ecuador">
    <meta property="og:description" content="Estudio Jurídico en Guayaquil con experiencia en derecho penal, civil, corporativo y más. Lisboa Legal Group, excelencia y compromiso con su caso.">
    <meta property="og:image" content="https://lisboalegalgroup.github.io/legal/daniel-espinoza-profile.jpg">
    <meta property="og:url" content="https://lisboalegalgroup.github.io/legal/">
    <meta property="og:type" content="website">"""
        content = re.sub(
            r'(<meta name="viewport"[^>]*>)',
            r'\1' + og_tags,
            content,
            count=1
        )

    # Make favicons absolute if not already
    content = re.sub(r'<link rel="icon" href="favicon', r'<link rel="icon" href="https://lisboalegalgroup.github.io/legal/favicon', content)
    content = re.sub(r'<link rel="shortcut icon" href="favicon.ico', r'<link rel="shortcut icon" href="https://lisboalegalgroup.github.io/legal/favicon.ico', content)
    content = re.sub(r'<link rel="apple-touch-icon" href="apple-touch-icon.png', r'<link rel="apple-touch-icon" href="https://lisboalegalgroup.github.io/legal/apple-touch-icon.png', content)

    # Enhance JSON-LD Schema
    schema_old = '"name": "Lisboa Legal Group",\n      "url": "https://lisboalegalgroup.github.io/legal/"'
    schema_new = '"name": "Lisboa Legal Group",\n      "alternateName": "Lisboa Legal",\n      "url": "https://lisboalegalgroup.github.io/legal/",\n      "logo": "https://lisboalegalgroup.github.io/legal/logo-full.png"'
    
    if '"alternateName"' not in content:
        content = content.replace(schema_old, schema_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        process_file(os.path.join(directory, filename))
print('SEO tags injected/updated successfully.')
