import os
import glob

old_css = """        .hero-video {
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

new_css = """        .hero-video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 0;
        }"""

def update_files():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if old_css in content:
                content = content.replace(old_css, new_css)
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    update_files()
