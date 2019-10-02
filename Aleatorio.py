# Aleatorio.py
# Autor: Hugo Bueno.
# Fecha de creacion: 14/09/2019

# python nos ayuda con muchas librerias listas para utilizarse.
# A esas librerias les da el nombre de module
# Para utilizar un modulo en un programa, primero debe importarse, usando la instruccion import.
import random

# Se define una variable float, y se le asigna un valor
numero1=float(10.5)

# se define una funcion
def miFuncion():
    # Se pasa a float todo numero aleatorio generado por random.randrange() 
    numero2=float(random.randrange(1,10))

    # Se ponen corchetes para asi imprimir sus salidas
    mensaje= "La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Se ejecuta la funcion 
miFuncion()