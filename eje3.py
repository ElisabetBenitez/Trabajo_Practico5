print("Ingrese su sueldo")
sueldo = int(input())
print("Ingrese número de rango del 1 al 3")
rango = int(input())


if rango == 1:
    print(sueldo * 0.83)
elif rango == 2:
    print(sueldo * 1.2)
elif rango == 3:
    print(sueldo * 5)
else:
    print("El valor no esta considerado dentro del rango")

