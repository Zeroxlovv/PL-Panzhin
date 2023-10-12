a=input()
c=0
while ':' in a:
    a=a.replace(':','%',1)
    c+=1
print(a,c)
