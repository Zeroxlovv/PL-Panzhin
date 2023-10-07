a=input('Введите предложение\n')
k=''
for i in range(len(a)//2):
    if a[i]=='п':
        k+='*'
    else:
        k+=a[i]
print(k)
