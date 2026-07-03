import re
import os

files = ['index.html', 'areas-de-practica.html']

replacements = {
    'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'img_derecho-civil_1.webp',
    'https://images.unsplash.com/photo-1543269865-cbf427effbad?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'img_derecho-de-familia_1.webp',
    'https://images.unsplash.com/photo-1505664194779-8beaceb93744?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'img_derecho-constitucional_1.webp',
    'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'img_compliance_1.webp',
    'https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'img_herencias-y-sucesiones_1.webp',
    'https://images.unsplash.com/photo-1521791136064-7986c2920216?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'img_derecho-laboral_1.webp',
    'https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'oficina-aerea.webp',
    
    # Bottom ones in index.html and areas-de-practica.html
    'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&q=80&w=800': 'oficina-aerea.webp',
    'https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&q=80&w=800': 'abogado-hero.webp',
}

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done replacements.")
