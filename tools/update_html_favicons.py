import os
import re

html_files = [
    "index.html", "areas-de-practica.html", "compliance.html", "consultoria-tributaria.html",
    "daniel-espinoza.html", "derecho-administrativo.html", "derecho-civil.html",
    "derecho-constitucional.html", "derecho-de-familia.html", "derecho-laboral.html",
    "derecho-penal.html", "derecho-procesal.html", "derecho-societario.html",
    "herencias-y-sucesiones.html", "karol-carvajal.html", "privacidad.html"
]

def update_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update metadata links
    # Old rel="icon"
    content = re.sub(
        r'<link rel="icon" href="favicon\.png" type="image/png">',
        '<link rel="icon" href="favicon.png" type="image/png" sizes="192x192">\n    <link rel="icon" href="favicon-48x48.png" type="image/png" sizes="48x48">',
        content
    )
    # Old apple-touch-icon
    content = re.sub(
        r'<link rel="apple-touch-icon" href="favicon\.png">',
        '<link rel="apple-touch-icon" href="apple-touch-icon.png">',
        content
    )
    
    # 2. Update img tags (favicon.png -> logo-full.png)
    # We only want to replace it in img tags, not links
    content = re.sub(
        r'<img([^>]+)src="favicon\.png"([^>]+)>',
        r'<img\1src="logo-full.png"\2>',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

if __name__ == "__main__":
    for html_file in html_files:
        update_file(html_file)
