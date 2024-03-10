def f(n):
    if len(n)%2==0:
        s1=0
        s2=0
        k=len(n)//2
        for i in range(0,k):
            s1+= int(n[i])
        for i in range(k,len(n)):
            s2+= int(n[i])
        if s1==s2:
            print("Номер счастливый")
        else:
            print("Номер не счастливый")
    else:
        print("Ошибка")
n=input("Введите номер билета: ")
print(f(n))