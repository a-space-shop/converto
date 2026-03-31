c=open('main.py','r',encoding='utf-8').read()
c=c.replace('StaticFiles(directory="../frontend", html=True)','StaticFiles(directory=".", html=True)')
open('main.py','w',encoding='utf-8').write(c)
print('Done!')