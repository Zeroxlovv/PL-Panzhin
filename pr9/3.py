def f():
    b=int(input()) #Вводи длины сторки
    for i in range(b):
        a=int(input()) #Ввод числа в последовательности
        if i%2==1:
            print(a)
        if a==0:
            break
f()
