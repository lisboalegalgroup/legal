import os
import re
import subprocess

directorio = r"c:\Users\ja_Ca\Desktop\lisboa legal group"

# Archivos a renombrar
renames = {
    'penal.html': 'derecho-penal.html',
    'civil.html': 'derecho-civil.html',
    'laboral.html': 'derecho-laboral.html',
    'familia.html': 'derecho-de-familia.html',
    'societario.html': 'derecho-societario.html',
    'procesal.html': 'derecho-procesal.html',
    'sucesiones.html': 'herencias-y-sucesiones.html',
    'administrativo.html': 'derecho-administrativo.html',
    'constitucional.html': 'derecho-constitucional.html'
}

# Nuevos H1 optimizados
h1_updates = {
    'penal.html': '<h1>Abogados Expertos en Derecho Penal</h1>',
    'civil.html': '<h1>Especialistas en Derecho Civil y Contratos</h1>',
    'laboral.html': '<h1>Abogados en Derecho Laboral y Empresarial</h1>',
    'familia.html': '<h1>Abogados en Derecho de Familia y Divorcios</h1>',
    'societario.html': '<h1>Asesoría en Derecho Societario y Corporativo</h1>',
    'procesal.html': '<h1>Abogados Procesalistas y Litigio Estratégico</h1>',
    'sucesiones.html': '<h1>Abogados Expertos en Herencias y Sucesiones</h1>',
    'administrativo.html': '<h1>Especialistas en Derecho Administrativo y Contratación Pública</h1>',
    'constitucional.html': '<h1>Defensa en Derecho Constitucional y Acciones de Protección</h1>'
}

h1_regex = re.compile(r'<h1.*?>.*?</h1>', re.IGNORECASE | re.DOTALL)

archivos = [f for f in os.listdir(directorio) if f.endswith('.html')]

# 1. Modificar el contenido de TODOS los archivos HTML (actualizar enlaces y H1 si corresponde)
for archivo in archivos:
    ruta_completa = os.path.join(directorio, archivo)
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # 1.1 Si el archivo está en h1_updates, actualizar su H1
        if archivo in h1_updates:
            # Reemplazar la primera coincidencia de <h1>
            nuevo_h1 = h1_updates[archivo]
            contenido = h1_regex.sub(nuevo_h1, contenido, count=1)
            
        # 1.2 Actualizar todos los enlaces que apunten a los archivos viejos
        for viejo, nuevo in renames.items():
            # Buscar href="viejo.html" y reemplazar por href="nuevo.html"
            # También cubre posibles rutas relativas como href="./viejo.html"
            contenido = re.sub(rf'href=["\'](?:[^"\']*/)?{re.escape(viejo)}["\']', f'href="{nuevo}"', contenido)
            # También para código en javascript si lo hubiera window.location.href='viejo.html'
            contenido = re.sub(rf'window\.location\.href=["\'](?:[^"\']*/)?{re.escape(viejo)}["\']', f'window.location.href="{nuevo}"', contenido)

        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(contenido)
            
    except Exception as e:
        print(f"Error modificando {archivo}: {e}")

# 2. Renombrar los archivos físicos e indicarle a git con git mv
for viejo, nuevo in renames.items():
    ruta_vieja = os.path.join(directorio, viejo)
    ruta_nueva = os.path.join(directorio, nuevo)
    if os.path.exists(ruta_vieja):
        print(f"Renombrando {viejo} a {nuevo}...")
        try:
            subprocess.run(["git", "mv", viejo, nuevo], cwd=directorio, check=True)
            print(f" Éxito: {nuevo}")
        except subprocess.CalledProcessError as e:
            print(f" Falló git mv, usando os.rename: {e}")
            os.rename(ruta_vieja, ruta_nueva)

print("Actualización de H1 y URLs completada.")
