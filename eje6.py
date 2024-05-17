def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    else:
        return num1 / num2

# Mostrar el menú y recibir la operación deseada
print("Calculadora Simple")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
operation = input("Ingrese el número correspondiente a la operación deseada: ")

# Solicitar los números para realizar la operación
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada
if operation == '1':
    print("Suma:", sumar(num1, num2))
elif operation == '2':
    print("Resta:", restar(num1, num2))
elif operation == '3':
    print("Multiplicación:", multiplicar(num1, num2))
elif operation == '4':
    print("División:", dividir(num1, num2))
else:
    print("Opción no válida.")