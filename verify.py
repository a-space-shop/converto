c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace('<link rel="canonical" href="https://converto.fyi" />', '<link rel="canonical" href="https://converto.fyi" />\n  <meta name="google-site-verification" content="W9ncBgeK0uVCOizMQI8ZlomkgFrAWiWlfJNonme7-Qs" />')
open('index.html', 'w', encoding='utf-8').write(c)
print('Done!')