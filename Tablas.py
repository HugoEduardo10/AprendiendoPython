# Tablas.py
# Autor: Hugo Bueno
# Fecha de creacion: 14/09/2019

for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    
    # print sin poner nada es un salto de renglon
    print()

    # en un for se pone otro for.
    for j in range(1,11):
        
        # Aqui i contiene el numero de la base de la tabla y j el elemento de la tabla.
        salida="{} X {} = {}"
        print(salida.format(i,j,i*j))
    
    else:
        # Al concluir con las iteraciones indicadas se ejecuta este codigo.
        print()
