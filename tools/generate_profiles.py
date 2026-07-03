import os
import re

def create_profile(base_html, file_name, title, name, lastname, role, desc, img, email, linkedin, phone, vcard_link, is_female=False):
    # Extract head, header, footer
    head_match = re.search(r'(<!DOCTYPE html>.*?</header>)', base_html, re.DOTALL)
    footer_match = re.search(r'(<footer class="new-footer">.*?</html>)', base_html, re.DOTALL)
    
    if not head_match or not footer_match:
        print(f"Could not extract base structure for {file_name}")
        return

    top_part = head_match.group(1)
    bottom_part = footer_match.group(1)
    
    # Modify title and og tags in top_part
    top_part = re.sub(r'<title>.*?</title>', f'<title>{name} {lastname} | Lisboa Legal Group</title>', top_part)
    top_part = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{name} {lastname} | Lisboa Legal Group">', top_part)
    top_part = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="https://lisboalegalgroup.github.io/legal/{img.replace(" ", "%20")}">', top_part)
    top_part = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://lisboalegalgroup.github.io/legal/{file_name}">', top_part)
    
    # Active state for current nav if needed (optional)
    
    # Change body to have profile-page class
    top_part = top_part.replace('<body>', '<body class="profile-page">')
    
    socio_text = "Socia" if is_female else "Socio"

    body_content = f"""
    <!-- PROFILE HERO -->
    <section class="profile-hero-section">
        <!-- BREADCRUMB -->
        <div class="container profile-breadcrumb" data-aos="fade-down" data-aos-duration="600">
            <a href="index.html">Inicio</a> <span>/</span> <a href="index.html#equipo">Equipo</a> <span>/</span> {name} {lastname}
        </div>

        <div class="container">
            <div class="profile-hero-flex">
                <div class="profile-hero-left" data-aos="fade-right" data-aos-duration="1000">
                    <img loading="lazy" src="{img}" alt="{name} {lastname}">
                </div>
                <div class="profile-hero-right">
                    <h1 class="profile-name" data-aos="fade-up" data-aos-delay="100" data-aos-duration="800">{name}</h1>
                    <h2 class="profile-lastname" data-aos="fade-up" data-aos-delay="200" data-aos-duration="800">{lastname}</h2>
                    <p class="profile-role" data-aos="fade-up" data-aos-delay="300" data-aos-duration="800">{socio_text}</p>
                    <p class="profile-desc" data-aos="fade-up" data-aos-delay="400" data-aos-duration="800">{desc}</p>
                    
                    <div class="profile-social-icons" data-aos="fade-up" data-aos-delay="500" data-aos-duration="800">
                        <a href="tel:{phone}" aria-label="Llamar"><i class="fas fa-phone-alt"></i></a>
                        <a href="mailto:{email}" aria-label="Enviar correo"><i class="fas fa-envelope"></i></a>
                        <a href="{linkedin}" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                        <a href="{vcard_link}" aria-label="Descargar vCard"><i class="fas fa-user-circle"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PROFILE TABS -->
    <section class="profile-tabs-section">
        <div class="container">
            <div class="profile-tabs-nav" data-aos="fade-up" data-aos-delay="600" data-aos-duration="800">
                <button class="profile-tab-btn active" onclick="openProfileTab(event, 'experiencia')">Experiencia</button>
                <button class="profile-tab-btn" onclick="openProfileTab(event, 'trayectoria')">Trayectoria profesional</button>
                <button class="profile-tab-btn" onclick="openProfileTab(event, 'estudios')">Estudios</button>
                <button class="profile-tab-btn" onclick="openProfileTab(event, 'reconocimientos')">Reconocimientos</button>
                <button class="profile-tab-btn" onclick="openProfileTab(event, 'membresias')">Membresías</button>
                <button class="profile-tab-btn" onclick="openProfileTab(event, 'publicaciones')">Publicaciones</button>
            </div>

            <div class="profile-tabs-content" data-aos="fade-up" data-aos-delay="700" data-aos-duration="800">
                <div id="experiencia" class="profile-tab-pane active">
                    <div class="profile-tab-content-text">
                        <p>Contenido pendiente de añadir. (Reemplazar con la experiencia de {name} {lastname}).</p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                    </div>
                </div>
                
                <div id="trayectoria" class="profile-tab-pane">
                    <div class="profile-tab-content-text">
                        <p>Contenido pendiente de añadir. (Reemplazar con la trayectoria de {name} {lastname}).</p>
                    </div>
                </div>
                
                <div id="estudios" class="profile-tab-pane">
                    <div class="profile-tab-content-text">
                        <p>Contenido pendiente de añadir. (Reemplazar con los estudios de {name} {lastname}).</p>
                    </div>
                </div>
                
                <div id="reconocimientos" class="profile-tab-pane">
                    <div class="profile-tab-content-text">
                        <p>Contenido pendiente de añadir. (Reemplazar con los reconocimientos de {name} {lastname}).</p>
                    </div>
                </div>
                
                <div id="membresias" class="profile-tab-pane">
                    <div class="profile-tab-content-text">
                        <p>Contenido pendiente de añadir. (Reemplazar con las membresías de {name} {lastname}).</p>
                    </div>
                </div>
                
                <div id="publicaciones" class="profile-tab-pane">
                    <div class="profile-tab-content-text">
                        <p>Contenido pendiente de añadir. (Reemplazar con las publicaciones de {name} {lastname}).</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- TABS JAVASCRIPT -->
    <script>
    function openProfileTab(evt, tabName) {{
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("profile-tab-pane");
        for (i = 0; i < tabcontent.length; i++) {{
            tabcontent[i].classList.remove("active");
        }}
        tablinks = document.getElementsByClassName("profile-tab-btn");
        for (i = 0; i < tablinks.length; i++) {{
            tablinks[i].classList.remove("active");
        }}
        document.getElementById(tabName).classList.add("active");
        evt.currentTarget.classList.add("active");
    }}
    </script>
    """
    
    full_html = top_part + "\n" + body_content + "\n" + bottom_part
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {file_name}")

# Read base file
with open('daniel-espinoza.html', 'r', encoding='utf-8', errors='ignore') as f:
    base_html = f.read()

# 1. Daniel Espinoza
create_profile(
    base_html=base_html,
    file_name="daniel-espinoza.html",
    title="Daniel Espinoza",
    name="Daniel",
    lastname="Espinoza",
    role="Socio",
    desc="Socio Fundador / Especialista Penal Militar. Lidera la estrategia legal y litigación.",
    img="Daniel Modelo.webp",
    email="lisboalegalgroup@gmail.com",
    linkedin="https://www.linkedin.com/company/lisboa-legal-group",
    phone="+593990967952",
    vcard_link="#",
    is_female=False
)

# 2. Karol Carvajal
create_profile(
    base_html=base_html,
    file_name="karol-carvajal.html",
    title="Karol Carvajal",
    name="Karol",
    lastname="Carvajal",
    role="Socia",
    desc="Especialista en derecho corporativo y civil.",
    img="Nueva foto karo.webp",
    email="lisboalegalgroup@gmail.com",
    linkedin="https://www.linkedin.com/company/lisboa-legal-group",
    phone="+593990967952",
    vcard_link="#",
    is_female=True
)

# 3. Gustavo San Andrés
create_profile(
    base_html=base_html,
    file_name="gustavo-san-andres.html",
    title="Gustavo San Andrés",
    name="Gustavo",
    lastname="San Andrés",
    role="Socio",
    desc="Experto en derecho empresarial y estrategias financieras.",
    img="gustavo.webp",
    email="lisboalegalgroup@gmail.com",
    linkedin="https://www.linkedin.com/company/lisboa-legal-group",
    phone="+593990967952",
    vcard_link="#",
    is_female=False
)
