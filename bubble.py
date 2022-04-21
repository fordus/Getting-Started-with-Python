
from array import array


# Bubble Sort
def bubble_sort(arr):
    length = len(arr) - 1 
    print(f"Se toma el length del array menos 1 elemento que sería: {length}")

    #Bucle pasa pasadas
    for i in range(0, length):
         
        print(f"{i + 1} pasada: {arr}")

        # Bucle comparaciones
        for j in range(0, length):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    

arr = [6,2,6,1,2,9,3,56,1,0,-2]
print("Antes de ordenar")
print(arr)
bubble_sort(arr)
print("Después de ordenar")
print(arr)
