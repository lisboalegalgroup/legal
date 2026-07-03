import codecs, re
content = codecs.open('index_recovered_utf8.html', 'r', 'utf-8').read()

hero_match = re.search(r'(<div class="hero-text">.*?</div>)', content, re.DOTALL)
if hero_match: print('HERO LOGO IN RECOVERED:\n', hero_match.group(1))

footer_match = re.search(r'(<div class="footer-brand">.*?</div>)', content, re.DOTALL)
if footer_match: print('\nFOOTER LOGO IN RECOVERED:\n', footer_match.group(1))
