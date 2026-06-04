import re

with open('calculadora-plazos.html', 'r', encoding='utf-8') as f:
    plazos = f.read()

with open('nueva calculadora jubilacion.html', 'r', encoding='utf-8') as f:
    jubi = f.read()

head_nav = plazos[:plazos.find('<section class="area-hero"')]
mobile_js_match = re.search(r'(// Mobile Menu y Header Scrolled.*?</script>)', plazos, re.DOTALL)
mobile_js = mobile_js_match.group(1) if mobile_js_match else ''

head_nav = head_nav.replace('Calculadora de Plazos Procesales | Lisboa Legal Group', 'Calculadora de Jubilación | Lisboa Legal Group')
head_nav = head_nav.replace('Calculadora de liquidación laboral gratuita y en línea para Ecuador. Calcule fácilmente beneficios e indemnizaciones.', 'Calculadora de pensiones jubilares referencial. Jubilación Patronal e IESS para Ecuador.')
head_nav = head_nav.replace('calculadora-plazos.html', 'calculadora-jubilacion.html')

hero = '''<section class="area-hero" style="background-image: linear-gradient(rgba(5, 20, 42, 0.90), rgba(5, 20, 42, 0.90)), url('img_derecho-laboral_2.webp'); background-size: cover; background-position: center; padding: 180px 0 80px 0;">
    <div class="container">
        <h1 style="color: var(--white); font-size: 3.2rem; margin-bottom: 20px; font-weight: 800;">Calculadora de Jubilación</h1>
        <div class="line" style="width: 70px; height: 3px; background-color: var(--accent-gold); margin: 0 auto 25px auto;"></div>
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.6;">
            Cálculo referencial de la pensión jubilar patronal, IESS y capital global. Aplicando Resolución CNJ No. 04-2026 y acuerdos ministeriales vigentes.
        </p>
    </div>
</section>
'''

styles_match = re.search(r'<style>(.*?)</style>', jubi, re.DOTALL)
styles = styles_match.group(1) if styles_match else ''
styles = re.sub(r'body\{.*?\}', '', styles)
styles = re.sub(r'\.hero\{.*?\}', '', styles)
styles = re.sub(r'\.hero::before\{.*?\}', '', styles)
styles = re.sub(r'\.hi\{.*?\}', '', styles)
styles = re.sub(r'\.logo\{.*?\}', '', styles)
styles = re.sub(r'\.hero h1.*?\}', '', styles)
styles = re.sub(r'\.hs\{.*?\}', '', styles)

tabs_match = re.search(r'(<div class="tabs-bar">.*?<div class="footer">.*?</div>)', jubi, re.DOTALL)
jubi_html = tabs_match.group(1) if tabs_match else ''

js_match = re.search(r'<script>(.*?)</script>', jubi, re.DOTALL)
jubi_js = js_match.group(1) if js_match else ''

final_html = head_nav + hero + '''
<style>
''' + styles + '''
</style>
<section class="section-padding bg-marble" style="min-height: 80vh; border-top: 3px solid var(--accent-gold); padding-top: 60px;">
    <div class="container">
''' + jubi_html + '''
    </div>
</section>
<script>
''' + jubi_js + '''
''' + mobile_js + '''
</body>
</html>
'''

with open('calculadora-jubilacion.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
