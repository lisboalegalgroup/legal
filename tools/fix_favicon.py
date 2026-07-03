import os
from PIL import Image

def make_transparent(input_path):
    print(f"Opening {input_path}...")
    img = Image.open(input_path)
    img = img.convert("RGBA")
    
    datas = img.getdata()
    
    newData = []
    threshold = 240
    for item in datas:
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    return img

def generate_assets():
    img = make_transparent("favicon_original.png")
    
    # 1. Full Logo (192x192) - for header/footer
    img_full = img.resize((192, 192), Image.Resampling.LANCZOS)
    img_full.save("logo-full.png", "PNG")
    print("Saved logo-full.png (192x192, transparent)")
    
    # 2. Icon only (Pillar) - for favicon/SEO
    # Crop top 60% of the 1024x1024 image to get just the pillar and book
    # Bounding box roughly: (220, 220, 800, 600)
    # Let's try to be safer and crop (0, 0, 1024, 650) then auto-crop
    img_icon = img.crop((0, 0, 1024, 650))
    
    # Auto-crop transparency
    bbox = img_icon.getbbox()
    if bbox:
        img_icon = img_icon.crop(bbox)
    
    # Make it square by adding padding
    w, h = img_icon.size
    new_size = max(w, h)
    new_img = Image.new("RGBA", (new_size, new_size), (255, 255, 255, 0))
    new_img.paste(img_icon, ((new_size - w) // 2, (new_size - h) // 2))
    
    # Save as favicon.png (main) and other sizes
    for size in [32, 48, 96, 144, 180, 192]:
        resized = new_img.resize((size, size), Image.Resampling.LANCZOS)
        if size == 192:
            resized.save("favicon.png", "PNG")
        elif size == 48:
            resized.save("favicon-48x48.png", "PNG")
        elif size == 180:
            resized.save("apple-touch-icon.png", "PNG")
            
    print("Saved pillar-only icons (favicon.png, favicon-48x48.png, apple-touch-icon.png)")

if __name__ == "__main__":
    generate_assets()
