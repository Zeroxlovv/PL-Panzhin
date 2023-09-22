a=input('Введите число ')
b=[]
c=[]
for i in a:
    if int(i)%2==0:
        b.append(i)
    else:
        c.append(i)
print(b,' - чётные цифры')
print(c,' - нечётные цифры')
