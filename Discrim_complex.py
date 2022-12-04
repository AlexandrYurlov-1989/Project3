import cmath
 
print("Введите коэф.для квадратного уравнени")
print("ax^2 + bx + c = 0:")
a=complex(input("a = "))
b=complex(input("b = "))
c=complex(input("c = "))
        
if a==0 and b==0 and c==0:
    print("X-принимает любое число")
elif a==0 and b==0:
    print ("решений нет")
elif a==0 and c==0:
    print("x=",0)
elif a==0:
    x=(-c/b)
    print("x=",x)
elif b==0:
    print("x=", cmath.sqrt(-c/a))
else:
    D = b ** 2 - 4 * a * c
    print(f"Дискриминант = {D}")
    x1=(-b+cmath.sqrt(D))/(2*a)
    x2=(-b-cmath.sqrt(D))/(2*a)
    x1 = complex(round(x1.real, 2),round(x1.imag, 2))
    x2 = complex(round(x2.real, 2),round(x2.imag, 2))
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    