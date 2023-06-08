import numpy as np
#Descargar numpy desde AVA y pegarlo en la ruta
#C:\Users\CETECOM\AppData\Local\Microsoft\WindowsApps
arreglo=np.arange(1,101)
print(arreglo)
#Reshape = Permite modificar la forma del arreglo
arreglo=arreglo.reshape((25,4))
print(arreglo)
arreglo = arreglo.reshape((10,10))
print(arreglo)
#Se puede escribir de cualquiera de las siguientes formas 
#Para pedir que me de un dato de cierta coordenada
print(arreglo[5,5])
print(arreglo[5][5])

#79
print(arreglo[7][8])

#100
#Cuando colocamos coordenadas negativas, el orden se invierte,
#Por lo que al trabajar con negativos, en vez de ser desde
#Izquiera a derecha, va de derecha a izquierda y de abajo hacia arriba
print(arreglo[-1,-1])
print(arreglo[9,9])

#Slice me permite mostrar una cantidad de valores
#Start:Stop:Step
#Mostrar desde la mitad y solo los primeros 5
print(arreglo[5::,:5:])

#Mostrar los primeros 3 datos y las primeras 4 filas
print(arreglo[:4,:3])

#Mostrar desde 61 hasta 80

print(arreglo[6:8,:])
#Mostrar el último dígito de cada fila
print(arreglo[0:,9:])

numero=int(input("Ingrese un número: "))
for y in range(10):
    for x in range(10):
        if arreglo[y,x]==numero:
            print(f"En la fila {y} y en la columna {x} se encuentra el valor{arreglo[y,x]}")