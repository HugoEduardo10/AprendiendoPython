# Entrada.py
# Autor: Hugo Bueno
# Fecha de creacion: 14/09/2019

entrada=input()
print(type(entrada))

# La variable booleana contiene el resultado de verificar si lo capturado es digito, y si no se encuentra un punto en lo capturado,
# lo que indicaria de que trata con un numero con decimales, es decir, float. 
# Si find retorna -1 quiere decir que lo buscado, en este  caso un punto decimal no se encontro.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    # Lineas que se realizaran si es Verdadera (True)
    print("Dato entero. Muy bien!")
else:
    # Lineas que se realizaran si es Falsa (False)
    print("Dato no es entero. Intentar nuevamente.")
    