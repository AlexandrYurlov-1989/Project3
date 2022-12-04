import math
 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a==0 and b==0 and c==0:
    print("X-принимает любое число")
elif a==0 and b==0:
    print ("решений нет")
elif a==0 and c==0:
    print("x=",0)
elif a==0:
    x=(-c/b)
    print("x=",x)
else:
    D = b ** 2 - 4 * a * c
    print(f"Дискриминант = {D}")
 
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        x1 = round(x1, 2)
        x2 = round(x2, 2)
        print(f"x1 = {x1} \nx2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        print("Корней нет")
