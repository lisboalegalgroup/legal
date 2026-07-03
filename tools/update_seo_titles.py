import os
import re

# Directorio que contiene los archivos HTML
directorio = r"C:\Users\ja_Ca\Desktop\lisboa legal group"

# Archivos específicos que se omitirán
archivos_excluidos = {'privacidad.html'}

# Define los nuevos valores de title y meta descripciones, enfocados en Guayaquil SEO
seo_data = {
    'index.html': {
        'title': 'Lisboa Legal Group | Abogados en Guayaquil, Ecuador',
        'desc': 'Estudio Jurídico en Guayaquil con experiencia en derecho penal, civil, corporativo y más. Lisboa Legal Group, excelencia y compromiso con su caso.'
    },
    'areas-de-practica.html': {
        'title': 'Áreas de Práctica | Abogados Especialistas en Guayaquil',
        'desc': 'Conoce nuestras áreas de práctica legal en Guayaquil. Especialistas en derecho corporativo, sucesiones, familia, penal y más. Contáctenos hoy.'
    },
    'sucesiones.html': {
        'title': 'Abogados de Herencias y Sucesiones en Guayaquil | Lisboa Legal',
        'desc': 'Asesoría experta en herencias, testamentos y sucesiones en Guayaquil. Protegemos su patrimonio familiar con eficiencia y transparencia.'
    },
    'societario.html': {
        'title': 'Abogados en Derecho Societario y Corporativo en Guayaquil',
        'desc': 'Especialistas en constitución de empresas, fusiones y asesoría corporativa en Guayaquil. Impulse su negocio con la mejor asesoría legal.'
    },
    'familia.html': {
        'title': 'Abogados de Familia y Divorcios en Guayaquil | Lisboa Legal',
        'desc': 'Abogados expertos en derecho de familia, divorcios, pensiones alimenticias y tenencia en Guayaquil. Trato empático y confidencial.'
    },
    'penal.html': {
        'title': 'Abogados Penalistas en Guayaquil | Defensa Legal Efectiva',
        'desc': 'Firma de abogados penalistas en Guayaquil. Defendemos sus derechos con estrategias sólidas y confidencialidad absoluta.'
    },
    'laboral.html': {
        'title': 'Abogados Laborales en Guayaquil | Defensa a Trabajadores y Empresas',
        'desc': 'Representación legal en conflictos laborales, despidos y asesoría corporativa en Guayaquil. Protegemos sus derechos laborales.'
    },
    'civil.html': {
        'title': 'Abogados de Derecho Civil en Guayaquil | Lisboa Legal Group',
        'desc': 'Especialistas en contratos, obligaciones y litigios civiles en Guayaquil. Asesoría legal confiable para proteger sus intereses.'
    },
    'administrativo.html': {
        'title': 'Abogados en Derecho Administrativo en Guayaquil',
        'desc': 'Asesoría legal en derecho público, procesos contenciosos y trámites ante entidades en Guayaquil. Expertos en regulación estatal.'
    },
    'compliance.html': {
        'title': 'Compliance Corporativo y Prevención Legal en Guayaquil',
        'desc': 'Asesoramiento en cumplimiento normativo y programas de compliance en Guayaquil. Evite riesgos legales en su empresa.'
    },
    'consultoria-tributaria.html': {
        'title': 'Consultoría y Asesoría Tributaria en Guayaquil | Lisboa Legal',
        'desc': 'Expertos en planificación fiscal y derecho tributario en Guayaquil. Optimizamos sus impuestos dentro del marco legal ecuatoriano.'
    },
    'constitucional.html': {
        'title': 'Abogados en Derecho Constitucional en Guayaquil',
        'desc': 'Defensa de garantías y derechos fundamentales. Acciones de protección y litigios constitucionales en Guayaquil con Lisboa Legal Group.'
    },
    'procesal.html': {
        'title': 'Abogados Procesalistas y Litigios (COGEP) en Guayaquil',
        'desc': 'Representación experta en todo tipo de procesos judiciales y audiencias bajo el COGEP en Guayaquil. Experiencia en tribunales.'
    },
    # Para perfiles de abogados
    'daniel-espinoza.html': {
        'title': 'Abg. Daniel Espinoza | Especialista Penal y Civil en Guayaquil',
        'desc': 'Conozca a Daniel Espinoza, abogado socio de Lisboa Legal Group en Guayaquil. Experto en litigación y estrategia legal corporativa.'
    },
    'karol-carvajal.html': {
        'title': 'Abg. Karol Carvajal | Especialista Familia y Civil en Guayaquil',
        'desc': 'Conozca a Karol Carvajal, abogada socia de Lisboa Legal Group en Guayaquil. Especialista en protección familiar y resolución de conflictos.'
    }
}

# Expresiones regulares para encontrar title y meta description
title_re = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)
desc_re = re.compile(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', re.IGNORECASE)

archivos = [f for f in os.listdir(directorio) if f.endswith('.html') and f not in archivos_excluidos]

archivos_modificados = []
archivos_sin_seo_data = []

for archivo in archivos:
    ruta_completa = os.path.join(directorio, archivo)
    
    if archivo in seo_data:
        nuevos_datos = seo_data[archivo]
        nuevo_title = f'<title>{nuevos_datos["title"]}</title>'
        nueva_desc = f'<meta name="description" content="{nuevos_datos["desc"]}">'
        
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Reemplazar title
            if title_re.search(contenido):
                contenido = title_re.sub(nuevo_title, contenido)
            else:
                # Si no hay title (raro, pero puede pasar), agregarlo al final del head
                contenido = contenido.replace('</head>', f'    {nuevo_title}\n</head>')
                
            # Reemplazar meta description
            if desc_re.search(contenido):
                contenido = desc_re.sub(nueva_desc, contenido)
            else:
                # Si no hay meta description, agregarlo bajo el title
                contenido = contenido.replace(nuevo_title, f'    {nueva_desc}\n    {nuevo_title}')
                
            with open(ruta_completa, 'w', encoding='utf-8') as f:
                f.write(contenido)
                
            archivos_modificados.append(archivo)
            
        except Exception as e:
            print(f"Error procesando {archivo}: {e}")
    else:
        archivos_sin_seo_data.append(archivo)

print(f"Archivos SEO actualizados: {len(archivos_modificados)}")
for f in archivos_modificados:
    print(f" - {f}")

if archivos_sin_seo_data:
    print(f"\\nAdvertencia: Faltó información SEO (diccionario vacío) para los siguientes {len(archivos_sin_seo_data)} archivos:")
    for f in archivos_sin_seo_data:
         print(f" - {f}")
