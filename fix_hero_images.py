import os
import subprocess
import re

files = [
    "derecho-administrativo.html",
    "derecho-civil.html",
    "derecho-constitucional.html",
    "derecho-de-familia.html",
    "derecho-laboral.html",
    "derecho-penal.html",
    "derecho-procesal.html",
    "derecho-societario.html",
    "consultoria-tributaria.html",
    "compliance.html",
    "herencias-y-sucesiones.html"
]

for f in files:
    try:
        # Get the original file content from the commit before the extraction
        result = subprocess.run(['git', 'show', f'b3765b799871a5334d1ea748335dfac1e04bea1f:{f}'], capture_output=True, text=True, check=True)
        old_content = result.stdout
        
        # Find the URL used in .area-hero
        match = re.search(r'\.area-hero\s*\{[^}]*url\([\'"]?(.*?)[\'"]?\)', old_content)
        if match:
            img_url = match.group(1)
            print(f"File {f} had image {img_url}")
            
            # Read current file
            with open(f, 'r', encoding='utf-8') as file:
                current_content = file.read()
                
            # Replace the <section class="area-hero"> with inline styles
            inline_style = f'<section class="area-hero" style="background-image: linear-gradient(rgba(5, 20, 42, 0.85), rgba(5, 20, 42, 0.85)), url(\'{img_url}\');">'
            new_content = current_content.replace('<section class="area-hero">', inline_style)
            
            # Write back
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f} successfully.")
        else:
            print(f"Could not find original image for {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
