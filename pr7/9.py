def f(n):
    k=0
    while n>0:
        k+=n%10
        n=n//10
    return k
a=int(input())
c=0
while a>0:
    a-=f(a)
    c+=1
print(c)
print('--2--')
from random import randint
def f1(n,b,c):
    q1=1
    q2=1
    q3=1
    w1=0
    w3=0
    w3=0
    w1=sum(n)/len(n)
    w2=sum(b)/len(b)
    w3=sum(c)/len(c)
    for i in n:
        q1*=i
    for i in b:
        q2*=i
    for i in c:
        q3*=i
    return q1,w1,q2,w2,q3,w3
a=int(input())
b=int(input())
c=int(input())
a1=[]
a2=[]
a3=[]
for i in range(a):
        a1.append(randint(1,100))
for i in range(b):
        a2.append(randint(1,100))
for i in range(c):
        a3.append(randint(1,100))
print(f1(a1,a2,a3))
