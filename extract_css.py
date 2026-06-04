import os
import glob
import re

directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
os.chdir(directory)

# 1. Ensure css dir exists
if not os.path.exists("css"):
    os.makedirs("css")

# 2. Extract CSS from index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

style_match = re.search(r'<style>(.*?)</style>', index_content, re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    print("CSS successfully extracted to css/style.css")
else:
    print("Could not find <style> block in index.html")
    exit(1)

# 3. Replace <style> block in all HTML files
html_files = glob.glob("*.html")
html_files = [f for f in html_files if not f.startswith("google")] # Exclude Google verification file

link_tag = '<link rel="stylesheet" href="css/style.css">'

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We replace <style>...</style> with the link tag
    new_content = re.sub(r'<style>.*?</style>', link_tag, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No inline <style> found in {file} (or already updated)")

print("Done extracting CSS.")
