import os
import re
from PIL import Image

def optimize_images_and_html(directory):
    exclude_imgs = {'favicon.png', 'favicon_original.png'}
    
    # 1. Convert local images to webp
    image_files = []
    print("Iniciando conversión de imágenes a WebP...")
    for f in os.listdir(directory):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f not in exclude_imgs:
            image_files.append(f)
            
    for img_file in image_files:
        try:
            img_path = os.path.join(directory, img_file)
            img = Image.open(img_path)
            webp_name = os.path.splitext(img_file)[0] + '.webp'
            webp_path = os.path.join(directory, webp_name)
            
            # Use 'RGB' mode if converting JPEG or PNG without alpha, or keep alpha if RGBA
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")
                
            img.save(webp_path, 'webp', quality=85)
            print(f"OK Convertido: {img_file} -> {webp_name}")
        except Exception as e:
            print(f"Error convirtiendo {img_file}: {e}")

    # 2. Update HTML files
    print("\nIniciando actualización de archivos HTML...")
    html_files = [f for f in os.listdir(directory) if f.lower().endswith('.html')]
    
    preconnect_tags = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com">
    """
    
    def process_url(m, is_url_func):
        if is_url_func:
            quote = m.group(1)
            url = m.group(2)
        else:
            attr = m.group(1)
            url = m.group(2)
            
        if url.startswith('http') or url.startswith('//') or url in exclude_imgs:
            return m.group(0)
            
        if url.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Prevent replacing if its a folder with a .png suffix or something alike, very edge case but safe
            new_url = os.path.splitext(url)[0] + '.webp'
            if is_url_func:
                return f'url({quote}{new_url}{quote})'
            else:
                return f'{attr}"{new_url}"'
        return m.group(0)

    def process_img(img_m):
        img_tag = img_m.group(0)
        if 'loading="lazy"' in img_tag or 'logo-img' in img_tag:
            return img_tag
        return re.sub(r'<img\s', '<img loading="lazy" ', img_tag, count=1, flags=re.IGNORECASE)

    for html_file in html_files:
        filepath = os.path.join(directory, html_file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update image extensions
        content = re.sub(r'(src=|href=)"([^"]+)"', lambda m: process_url(m, False), content)
        content = re.sub(r'url\((["\']?)(.*?)\1\)', lambda m: process_url(m, True), content)
        
        # Add loading="lazy" to <img>
        content = re.sub(r'<img\s+[^>]+>', process_img, content, flags=re.IGNORECASE)
        
        # Add preconnect if not present
        if 'preconnect" href="https://fonts.googleapis.com"' not in content:
            if '<link' in content:
                content = content.replace('<link', preconnect_tags.strip() + '\n    <link', 1)
            elif '<head>' in content:
                content = content.replace('<head>', '<head>\n    ' + preconnect_tags.strip(), 1)
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"OK Modificado HTML: {html_file}")

if __name__ == "__main__":
    optimize_images_and_html(".")
