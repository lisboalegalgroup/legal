import re
import os

html_path = 'c:/Users/ja_Ca/Desktop/lisboa legal group/index.html'
out_path = 'c:/Users/ja_Ca/Desktop/lisboa legal group/areas-de-practica.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract from start to </header>
header_match = re.search(r'(.*?<\/header>)', content, flags=re.DOTALL)
if header_match:
    head_and_header = header_match.group(1)
    
    # We should update the Title in the header
    head_and_header = re.sub(r'<title>.*?<\/title>', '<title>Áreas de Práctica | Lisboa Legal Group</title>', head_and_header)
    
    # Change nav link in areas-de-practica.html so 'Inicio' is just index.html, which is already there. Wait, 'Áreas de Práctica' link goes to areas-de-practica.html now.
else:
    print("Header not found")
    exit(1)

# Extract <section id="servicios" ...> to its closing </section>
servicios_match = re.search(r'(<section id="servicios".*?<\/section>)', content, flags=re.DOTALL)
if servicios_match:
    servicios_section = servicios_match.group(1)
else:
    print("Servicios section not found")
    exit(1)

# Let's create a small page hero for the subpage
hero_html = """
<section class="hero" style="min-height: 40vh; padding: 120px 0 60px 0; background-color: var(--primary-blue); display: flex; align-items: center; justify-content: center; text-align: center;">
    <div class="container hero-container" style="z-index: 2; position: relative;">
        <h1 style="color: var(--white); font-size: 3rem; margin-bottom: 15px;">Nuestros <span style="color: var(--accent-gold);">Servicios</span></h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; max-width: 600px; margin: 0 auto;">Defendemos sus intereses con la excelencia y el rigor que nos caracteriza.</p>
    </div>
</section>
"""

# Now write "Servicios Complementarios"
complementarios_html = """
<section id="servicios-complementarios" class="section-padding bg-marble" style="border-top: 2px solid var(--accent-gold);">
    <div class="container">
        <div class="section-title">
            <h2>Servicios Complementarios</h2>
            <div class="line"></div>
            <p style="margin-top: 20px; font-size: 1.1rem;">Brindamos soluciones especializadas adicionales a nuestros clientes.</p>
        </div>
        
        <div class="services-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
            <!-- Complementary Service 1 -->
            <div class="service-card" style="background-image: linear-gradient(var(--overlay-color), var(--overlay-color)), url('https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&q=80&w=800'); height: 300px;">
                <div class="service-content">
                    <i class="fas fa-chart-line" style="color: var(--accent-gold); font-size: 2.5rem; margin-bottom: 15px;"></i>
                    <h3 style="color: white; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Montserrat', sans-serif; font-weight: 700; text-transform: uppercase;">Asesoría Financiera Legal</h3>
                    <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.9);">Análisis integral de los riesgos y oportunidades legales en inversiones y transacciones financieras corporativas.</p>
                </div>
            </div>
            
            <!-- Complementary Service 2 -->
            <div class="service-card" style="background-image: linear-gradient(var(--overlay-color), var(--overlay-color)), url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80&w=800'); height: 300px;">
                <div class="service-content">
                    <i class="fas fa-globe" style="color: var(--accent-gold); font-size: 2.5rem; margin-bottom: 15px;"></i>
                    <h3 style="color: white; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Montserrat', sans-serif; font-weight: 700; text-transform: uppercase;">Derecho Internacional</h3>
                    <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.9);">Representación y arbitraje en conflictos transfronterizos, garantizando el cumplimiento normativo internacional.</p>
                </div>
            </div>
            
            <!-- Complementary Service 3 -->
            <div class="service-card" style="background-image: linear-gradient(var(--overlay-color), var(--overlay-color)), url('https://plus.unsplash.com/premium_photo-1661414415246-3e502e2fb241?auto=format&fit=crop&q=80&w=800'); height: 300px;">
                <div class="service-content">
                    <i class="fas fa-hand-holding-usd" style="color: var(--accent-gold); font-size: 2.5rem; margin-bottom: 15px;"></i>
                    <h3 style="color: white; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Montserrat', sans-serif; font-weight: 700; text-transform: uppercase;">Recuperación de Cartera</h3>
                    <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.9);">Gestión extrajudicial y judicial altamente efectiva para la recuperación de activos y deudas corporativas.</p>
                </div>
            </div>
        </div>
    </div>
</section>
"""

# Extract the Call To Action / Contact mapping section
contact_match = re.search(r'(<section id="contacto".*?<\/section>)', content, flags=re.DOTALL)
contact_html = contact_match.group(1) if contact_match else ""

# Extract footer to end
footer_match = re.search(r'(<footer>.*<\/html>)', content, flags=re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
else:
    print("Footer not found")
    exit(1)

# Assemble everything
new_page = f"""{head_and_header}
{hero_html}
{servicios_section}
{complementarios_html}
{contact_html}
{footer_html}
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(new_page)

print(f"File created successfully at {out_path}")
