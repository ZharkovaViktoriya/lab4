from datetime import date
def f(day,month,year):
    try:
        d=date(year,month,day)
    except:
        print("Неверный ввод даты")
    if day*month==int(str(year)[2:]):
        return True
    else:
        return False
l=input().split(".")
l=list(map(int,l))
a,b,c=l
print(f(a,b,c))