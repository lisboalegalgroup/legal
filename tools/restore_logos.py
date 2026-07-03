import codecs

content = open('index.html', 'r', encoding='utf-8').read()

lockup = '''<div class="slg-lockup">
    <div class="slg-letters">SLG</div>
    <div class="slg-rule-wrap">
        <div class="slg-rule"></div><div class="slg-dot"></div><div class="slg-rule"></div>
    </div>
    <div class="slg-firm">San Andrés Legal Group</div>
</div>'''

hero_img = '<img loading="lazy" src="logo-full.png" alt="Lisboa Legal Group" class="hero-logo-large">'
footer_img = '<img loading="lazy" src="logo-full.png" alt="Lisboa Legal Group Logo" class="logo-img" style="max-width: 150px; margin-bottom: 20px;">'

if content.count(lockup) >= 2:
    parts = content.split(lockup, 2)
    new_content = parts[0] + hero_img + parts[1] + footer_img + parts[2]
    open('index.html', 'w', encoding='utf-8').write(new_content)
    print('Replaced lockups with images in index.html')
else:
    print('Lockups not found or count is less than 2.')
