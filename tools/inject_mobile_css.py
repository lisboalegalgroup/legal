import os
import glob
import re

css_to_inject = """
        @media (max-width: 900px) {
            .hero-container {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .hero-text p {
                margin: 0 auto 30px auto;
            }

            .menu-toggle {
                display: block;
                color: var(--white);
                font-size: 1.8rem;
                cursor: pointer;
                transition: color 0.3s;
                margin-left: auto;
            }

            .menu-toggle:hover {
                color: var(--accent-gold);
            }

            .nav-links {
                position: absolute;
                top: 100%; /* Just below the header */
                left: 0;
                width: 100%;
                background-color: rgba(5, 20, 42, 0.98); /* Brand dark blue */
                flex-direction: column;
                align-items: center;
                gap: 20px;
                padding: 30px 0;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                
                /* Hidden by default on mobile, but animatable */
                max-height: 0;
                overflow: hidden;
                opacity: 0;
                visibility: hidden;
                transition: all 0.4s ease;
            }
            
            .nav-links.active {
                max-height: 400px;
                opacity: 1;
                visibility: visible;
            }

            .nav-links li {
                width: 100%;
                text-align: center;
            }

            .nav-links a {
                display: block;
                padding: 10px;
                font-size: 1.1rem;
            }
            
            .lang-switch, .mobile-hidden {
                 display: none !important; /* hide lang switch inside nav on mobile to keep it simple */
            }
            
            .forms-wrapper {
                grid-template-columns: 1fr;
            }

            .hero-image-wrapper {
                max-width: 100%;
                margin: 0 auto;
                min-height: 350px;
            }

            .presence-container {
                grid-template-columns: 1fr;
            }
        }
"""

directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
os.chdir(directory)

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Check if the specific nav-links mobile CSS already exists to avoid duplication
    if "visibility: hidden;" in content and "max-height: 0;" in content and "max-height: 400px;" in content:
        # If it exists, let's just make sure margin-left: auto is in menu-toggle
        # We did this partially, but since we are redefining the entire block, we can replace the old block
        # Actually it's easier to remove the old @media that contains nav-links { position: absolute; } ... and inject
        old_media_match = re.search(r'@media\s*\(max-width:\s*900px\)\s*\{[^\}]*\.nav-links\s*\{\s*position:\s*absolute;[^\}]*\}[^\}]*\.nav-links\.active\s*\{[^\}]*\}[^\}]*\}', content, re.DOTALL)
        if old_media_match:
            # We must be careful because a media query can contain nested braces correctly matched? No, re.DOTALL with [^\}]* doesn't handle nested braces well, but css blocks inside @media have {}
            # So [^\}]* will stop at the first }. It's better to just replace the nav-links styling block inside.
            pass
            
    # Universal approach: if 'max-height: 400px;' is NOT in the file, we just inject the whole block before </style>
    if "max-height: 400px;" not in content:
        content = content.replace("</style>", css_to_inject + "\n    </style>")
    else:
        # Need to fix the .menu-toggle inside
        content = re.sub(
            r'(\.menu-toggle\s*\{\s*display:\s*block;\s*color:\s*var\(--white\);\s*font-size:\s*1\.8rem;\s*cursor:\s*pointer;\s*transition:\s*color\s*0\.3s;\s*)(?!margin-left:\s*auto;)',
            r'\1margin-left: auto;\n            ',
            content
        )
        
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(file)
