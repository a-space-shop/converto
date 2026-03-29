c=open('main.py','r',encoding='utf-8').read()
c=c.replace('C:/Users/abram/AppData/Local/Temp/converto','/tmp/converto')
open('main.py','w',encoding='utf-8').write(c)
print('Done!')