import sys

sueldo = int(sys.argv[1])
rango = int(sys.argv[2])


if rango == 1:
    print("La asignación es: ",sueldo * 0.83)
elif rango == 2:
    print("La asignación es: ",sueldo * 1.2)
elif rango == 3:
    print("La asignación es: ", sueldo * 5)
else:
    print("El valor no esta considerado dentro del rango")