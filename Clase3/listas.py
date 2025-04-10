#Practica sobre listas

array = ["futbol","Pc",18.6,18,[6,7,10.4],True,False]
print(array)
print(array[1]) 
print(array[4]) 
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])

#Cantidad de datos que cuenta el array

print(len(array))
 
#Agregar un valor dentro de la lista
array.append(66)
print(array)
#Insertar datos en una posicion
array.insert(1,88)
print(array)
#Insertar mas de un dato al final
array.extend([1,88,True,100])
print(array)

array1 = ["futbol","Pc",18.6,18,[6,7,10.4],True,False,"PC"]
array2 = [200,250,"hola"]
array3 = array1 + array2
print(array3)
#Buscar valores dentro de un array
print("PC" in array1)
#Saber el indice donde esta lo que busco
print(array1.index("PC"))
#Cantidad de veces que tengo el valor en mi array
print(array1.count("PC"))
#Eliminar valores del array
array1.remove("PC")
print(array1)
#Limpiar
array1.clear()
print(array1)
#Cambiar la posicion
array1.reverse()
print(array1)
#Ordenar de mayor a menor
array4= [1,2,8,-11,5]
array4.sort()
print(array4)
array4.sort(reverse=True)
print(array4)