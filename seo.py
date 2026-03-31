c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace('<title>Converto — Document Converter</title>', '<title>Converto - Free Online Document Converter | PDF, Word, Excel</title>')
open('index.html', 'w', encoding='utf-8').write(c)
print('Done!')