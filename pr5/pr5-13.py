a=input('Введите предложение с одной отрк. скобкой и одной закр. скобкой\n')
c = 0
k=''
while a[c] != '(':
    c+= 1
c+= 1
while a[c] != ')':
    k+=a[c]
    c+= 1
print(k)