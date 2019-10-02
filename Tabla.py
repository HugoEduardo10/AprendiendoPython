# Tabla.py
# Autor: Hugo Bueno
# Fecha de creacion: 14/09/2019

numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)

# for ejecuta un bloque de codigo un numero determinado de veces.
# El segundo parametro de range no se incluye en la serie de valores. Aqui seria del 1 al 10.
for i in range(1,11):

    # i va variando a cada iteracion
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))