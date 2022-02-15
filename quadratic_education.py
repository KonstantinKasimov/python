import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

d = b**2-4*a*c
if d<0:
    print("Корней нет")
elif d>0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Первый корень" , "%.4f"%x1)
    print("Второй корень" , "%.4f"%x2)
elif d==0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print("Единственный корен", "%.4f"%x1)