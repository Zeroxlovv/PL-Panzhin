a=input('Введите предложение\n')
c=0
while 'а' in a:
    a=a.replace('а','о',1)
    c+=1
while 'А' in a:
    a=a.replace('А','О',1)
    c+=1
print(a,c)
