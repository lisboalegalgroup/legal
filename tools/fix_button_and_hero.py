import os
import glob

old_btn_style = 'style="display: flex; align-items: center; gap: 20px; position: relative; right: -70px;"'
new_btn_style = 'style="display: flex; align-items: center; gap: 20px;"'

old_hero_css = """        .hero-video {
            position: absolute;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: 0;
            transform: translate(-50%, -50%);
            object-fit: cover;
        }"""

new_hero_css = """        .hero-video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transform: scale(1.05);
            z-index: 0;
        }"""

def update_files():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            modified = False
            if old_btn_style in content:
                content = content.replace(old_btn_style, new_btn_style)
                modified = True
                
            if old_hero_css in content:
                content = content.replace(old_hero_css, new_hero_css)
                modified = True
                
            if modified:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    update_files()
