def main():
    
    print("""
1.- Suma
2.- Resta
3.- Multplicacion
4.- Division
          """)
    respuesta = input("Ingrese la operacion a realizar: ")
    
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    
    
    if respuesta == '1':
        resultado = sumar(num1,num2)
    elif respuesta == '2':
        resultado = restar(num1, num2)
    elif respuesta == '3':
        resultado = multiply(num1, num2)
    elif respuesta == '4':
        if num2 == 0:
            print("No se puede dividir entre 0")
        else:
            resultado = dividir(num1, num2)
    
    print(f"El resultado es: {resultado}")
    
    