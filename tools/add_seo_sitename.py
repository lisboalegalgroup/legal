import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<head>' not in content.lower():
        return

    # Check if we already have the custom site_name meta tag to avoid duplicating
    if 'og:site_name' in content:
        print(f"Skipping {filepath}: og:site_name already present")
        return

    seo_content = """
    <!-- SEO Site Name Configuration -->
    <meta property="og:site_name" content="Lisboa Legal Group">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Lisboa Legal Group",
      "url": "https://lisboalegalgroup.github.io/"
    }
    </script>
    <link rel="apple-touch-icon" href="/favicon.png">
    <link rel="shortcut icon" href="/favicon.png">
"""

    # Update relative favicon paths to absolute to prevent 404s and SEO issues.
    content = content.replace('<link rel="icon" href="favicon.png"', '<link rel="icon" href="/favicon.png"')

    if not re.search(r'</head>', content, re.IGNORECASE):
        return
        
    new_content = re.sub(r'(</head>)', rf'{seo_content}\1', content, count=1, flags=re.IGNORECASE)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

def main():
    directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file in html_files:
        process_file(file)

if __name__ == '__main__':
    main()
