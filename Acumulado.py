# Acumulado.py
# Autor: Hugo Bueno
# Fecha de creacion: 14/09/2019


# Se declaran las variables que utilizaremos
acumulado=int(0)
numero=str("")

# Al colocar True como condicion de while, se forma un ciclo infinito que no se dejara de repetir hasta ver un break
while True:
    numero=input("Dame un numero entero: ")
    
    if numero=="":
        
        # Si el numero es vacio, acaba el programa.
        print("Vacio. Salida del programa.")
        break
    
    else:
      
        # Si se da valor acumulado = acumulado + numero.
        # Se realiza el calculo usando suma e igual(+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))


