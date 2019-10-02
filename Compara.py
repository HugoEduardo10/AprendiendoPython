# Compara.py
# Autor: Hugo Bueno
# Fecha de creacion: 14/09/2019

numero1=input("Numero 1: ")
numero2=input("Numero 2: ")
salida= "Numeros proporcionados: {} y {}. {}."

if (numero1==numero2):
    # Entra aqui los numeros definidos iguales
    print(salida.format(numero1,numero2, "Los numeros son iguales"))

else:
    # Se capturan if dentro de otro if.
    # Si los numeros no son iguales.
    if (numero1>numero2):
        # Reporta si el primero es mayor al segundo.
        print(salida.format(numero1,numero2, "El mayor es el primero"))
    else:
        # O al contrario, si el primero no es mayor al segundo.
        print(salida.format(numero1,numero2, "El mayor es el segundo"))
