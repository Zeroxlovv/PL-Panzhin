for n in range(100):
    s=f"{n:b}"
    if n%3==0:
        s=s+s[-3:]
    else:
        s=s+f"{(n%3)*3:b}"
    if int(s,2)<76:
        print(n)
