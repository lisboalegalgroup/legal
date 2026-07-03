import os
import glob
from PIL import Image

src_dir = r'C:\Users\ja_Ca\.gemini\antigravity\brain\b5cabcfd-3b6a-41e9-8e12-1ea599551ef6'
dest_dir = r'c:\Users\ja_Ca\Desktop\lisboa legal group'

mapping = {
    'fam_divorcio': 'img_derecho-de-familia_1.webp',
    'fam_pension': 'img_derecho-de-familia_2.webp',
    'fam_tenencia': 'img_derecho-de-familia_3.webp',
    'fam_acuerdos': 'img_derecho-de-familia_4.webp',
    'const_proteccion': 'img_derecho-constitucional_1.webp',
    'const_habeas': 'img_derecho-constitucional_2.webp'
}

for pattern, new_name in mapping.items():
    files = glob.glob(os.path.join(src_dir, f"{pattern}_*.png"))
    if not files:
        print(f"Skipping {pattern}, no files found.")
        continue
    
    latest_file = max(files, key=os.path.getmtime)
    img = Image.open(latest_file)
    dest_path = os.path.join(dest_dir, new_name)
    img.save(dest_path, "WEBP", quality=85)
    print(f"Saved {latest_file} -> {dest_path}")
