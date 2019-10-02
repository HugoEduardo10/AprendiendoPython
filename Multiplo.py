# Multiplo.py
# Autor: Hugo Bueno
# Fecha de creacion : 14/09/2019


# Se captura un numero y se almacena una vez que se ha convertido a int.
numero=int(input("Dame un numero entero: "))

# Se almacenan en valores booleanos la evaluacion de residuo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)

# Cuando se usa and, se resuelve por verdadero si son verdaderas.
# Cuando se usa or,  se resuelve por verdadero si al menos una es verdadera.
# Los parentesis le dicen a python que las primeras dos condiciones son juntas, y la tercera es independiente.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")