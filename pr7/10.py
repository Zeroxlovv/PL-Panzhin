def f(n):
    k=0
    if 210<n<231:
        for i in range(100,n+1):
            z=str(i)
            if a in z and b in z and c in z:
                k+=1
        return k
    else:
        print("n не принадлежит отрезку [210;231]")
a=input()#Цифры
b=input()#Цифры
c=input()#Цифры
n=int(input())
print(f(n))
print('-----2-----')
a=input('Введите предложение \n')
def f1(n):
    c=''.join(reversed(n))
    return c
'''a=a.split()
a.reverse()
f=" ".join(a)
print(f)'''
print(f1(a))
