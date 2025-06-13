num1 = 0
num2 = 0
resultado = 0

print("=========[ CALCULADORA ]==========")
print("1 SUMAR")
print("2. RESTAR")
print("3. MULTIPLICAR")
print("4. DIVIDIR")
print("5. SALIR")


while True:
    opc = int(input("Ingrese una opcion: "))
    
    num1 = int(input("Ingrese el primer numero: "))
    mum2 = int(input("Ingrese el segundo numero: "))
    
    if opc == 1:
        resultado = num1 + num2
        print(f"El resultado es: {resultado}")
    elif opc == 5:
        break
    
print("GRACIAS!!!")