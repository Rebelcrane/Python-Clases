arreglo = [1,2,3,4,5]
arreglo_p = ["Colombia" "Venezuela" "Mexico" "Haiti"]

#for elemento in arreglo_p: recorre todo el arreglo
    #print(elemento)
    
#for _ in range(6): para recorrer 6 veces
    #print("Hola")
    
#contador = 1
    
#while contador == 6:
    #print("Hola mundo")  
    #contador +=1
    

#cont = 0   
#while cont < 10:
    #print("Hola 2")
    #cont +=1
    #if cont == 5: 
        #break
        
#for i in range(10):
    #if i == 5 or i == 2:
        #continue
    #print(i)
    

    #Ordenar un arreglo de numeros de menor a mayor sin funciones 
    
arreglo_desordenado = [5,4,3,1,2]
n = len(arreglo_desordenado)
for i in range(n):
    for j in range(0, n-i-1):
        if arreglo_desordenado[j] > arreglo_desordenado[j+1]:
            arreglo_desordenado[j],arreglo_desordenado[j+1] = arreglo_desordenado[j+1],arreglo_desordenado[j]
    #print("Es Mayor")
print(arreglo_desordenado)

#Tarea: Obtener todos valores pares del siguiente arreglo y ponerlos en un arreglo nuevo

arreglo_pares_inpares = [20,498,40197,2]