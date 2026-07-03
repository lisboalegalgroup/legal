import os
import glob

old_hero_class = """        .hero {
            background-color: var(--primary-blue);
            color: var(--white);
            height: 85vh;
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
        }"""

new_hero_class = """        .hero {
            background-color: var(--primary-blue);
            color: var(--white);
            min-height: 100vh;
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
        }"""

def update_files():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if old_hero_class in content:
                content = content.replace(old_hero_class, new_hero_class)
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    update_files()
