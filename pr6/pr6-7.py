n=int(input())
a=[]
for i in range(n):
    a.append(input())
c=0 #сумма
k=1 # произведение 
for i in range(len(a)):
    if i%2==0:
        c+=int(a[i])
    else:
        k*=int(a[i])
print(c,k)
mx,mn=a.index(max(a)),a.index(min(a))
a[mn],a[mx]=a[mx],a[mn]
print(a)
