a=[]
for i in range(16):
    a.append(input())
c=set()
for i in a:
    if a.count(i)>1:
        c.add(i)
print(c,len(c))
print('Замена элемента')
print(a)
for i in range(len(a)):
    if int(a[i])<10:
        a[i]=0
    if int(a[i])>20:
        a[i]=1
print(a)
