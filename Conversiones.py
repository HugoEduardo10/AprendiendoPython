# Conversiones.py
# Autor: Hugo Bueno
# Fecha de Creacion: 14/09/2019

# Se declara una variable str 
numero="1234"
# Nos da el tipo que tiene la variable. La salida Type()
# no es un str, es un dato Type.
print (type(numero))
# Se convierte la cadena a int.
numero=int(numero)
# Noa da como la cadena ha cambiado
print (type(numero))
# Se declara un str con meta sustitucion 
salida="El numero utilizado es {}"
# Nos da el resultado. La meta sustitucion hara que donde esta {}
print(salida.format(numero)) 