import os
import glob

directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
os.chdir(directory)

css_to_add = """        .nav-links {
            display: flex;
            gap: 25px;
            list-style: none;
            margin: 0;
            padding: 0;
            align-items: center;
        }

        .nav-links a {"""

html_files = glob.glob("*.html")
if "index.html" in html_files:
    html_files.remove("index.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if .nav-links { already exists
    if ".nav-links {" not in content:
        # We replace the first occurrence of `.nav-links a {`
        if "        .nav-links a {" in content:
            content = content.replace("        .nav-links a {", css_to_add, 1)
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed {file}")
        else:
            print(f"Could not find exact text in {file}")
    else:
        print(f"Already fixed or has .nav-links {{ {file}")
