import os
import glob
import re

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Inject HTML Menu Toggle
    # Look for the nav-links ul. Before it, insert the menu-toggle div.
    if 'class="menu-toggle"' not in content:
        # Match <nav> \s* <ul class="nav-links">
        content = re.sub(
            r'(<nav>\s*<ul class="nav-links">)',
            r'<div class="menu-toggle" id="mobile-menu">\n                    <i class="fas fa-bars"></i>\n                </div>\n                \1',
            content,
            flags=re.IGNORECASE,
            count=1
        )

    # 2. Update CSS for mobile menu
    # Replace the existing media query that hides the menu
    old_css = r'@media \(max-width: 900px\) \{\s*\.hero-container \{[^\}]*\}\s*\.hero-text p \{[^\}]*\}\s*\.nav-links \{\s*display:\s*none;\s*\}'
    
    if re.search(old_css, content):
        new_css = """@media (max-width: 900px) {
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
            }"""
        content = re.sub(old_css, new_css, content, count=1)
    
    # 3. Inject JavaScript
    # Look for </body> and inject the script right before it
    js_code = """
    <!-- Mobile Menu Toggle Script -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenu = document.getElementById('mobile-menu');
            const navLinks = document.querySelector('.nav-links');
            const menuIcon = mobileMenu ? mobileMenu.querySelector('i') : null;

            if (mobileMenu && navLinks && menuIcon) {
                mobileMenu.addEventListener('click', function(e) {
                    e.stopPropagation(); // Prevenir burbujeo
                    navLinks.classList.toggle('active');
                    
                    // Toggle icono Hamburguesa/Cruz
                    if (navLinks.classList.contains('active')) {
                        menuIcon.classList.remove('fa-bars');
                        menuIcon.classList.add('fa-times');
                    } else {
                        menuIcon.classList.remove('fa-times');
                        menuIcon.classList.add('fa-bars');
                    }
                });

                // Cerrar menú al hacer clic en un enlace (útil para Single Page)
                const links = navLinks.querySelectorAll('a');
                links.forEach(link => {
                    link.addEventListener('click', () => {
                        navLinks.classList.remove('active');
                        menuIcon.classList.remove('fa-times');
                        menuIcon.classList.add('fa-bars');
                    });
                });
                
                // Cerrar menú al hacer click fuera
                document.addEventListener('click', function(event) {
                    const isClickInsideMenu = navLinks.contains(event.target);
                    const isClickOnToggle = mobileMenu.contains(event.target);
                    
                    if (!isClickInsideMenu && !isClickOnToggle && navLinks.classList.contains('active')) {
                        navLinks.classList.remove('active');
                        menuIcon.classList.remove('fa-times');
                        menuIcon.classList.add('fa-bars');
                    }
                });
            }
            
            // Script para header scrolleado si no existe
            const header = document.querySelector('header');
            if (header) {
                window.addEventListener('scroll', () => {
                    if (window.scrollY > 50) {
                        header.classList.add('scrolled');
                    } else {
                        header.classList.remove('scrolled');
                    }
                });
            }
        });
    </script>
"""
    if 'id="mobile-menu"' in content and '<script>\n        document.addEventListener(\'DOMContentLoaded\', function() {\n            const mobileMenu = document.getElementById(\'mobile-menu\');' not in content:
        # Avoid duplicate injections
        if '<!-- Mobile Menu Toggle Script -->' not in content:
            content = content.replace('</body>', f'{js_code}</body>')
            
    # Also inject the original CSS rules for the menu toggle (hide on desktop)
    # Right before </style>
    if '.menu-toggle {' not in content and '</style>' in content:
        desktop_css = """
        /* Hide menu toggle on desktop by default */
        .menu-toggle {
            display: none;
        }
        """
        content = content.replace('</style>', f'{desktop_css}\n    </style>')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes needed for {filepath}")

def main():
    directory = r"c:\Users\ja_Ca\Desktop\lisboa legal group"
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file in html_files:
        process_html_file(file)

if __name__ == '__main__':
    main()
