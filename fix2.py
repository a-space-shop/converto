c=open('main.py','r',encoding='utf-8').read()
c=c.replace('../frontend/index.html','index.html')
open('main.py','w',encoding='utf-8').write(c)
print('Done!')