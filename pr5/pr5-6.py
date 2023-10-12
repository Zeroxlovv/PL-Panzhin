a=input()
c=0
while 'а' in a:
    a=a.replace('а','',1)
    c+=1
while 'А' in a:
    a=a.replace('А','',1)
    c+=1
print(a,c)
