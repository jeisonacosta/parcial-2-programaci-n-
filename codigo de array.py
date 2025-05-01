def invertir_array(arr):
    return arr[::-1]

try:
    cantidad = int(input("¿Cuántos elementos tendrá el array? "))

    if cantidad <= 0:
        print("Debe ingresar un número entero positivo.")
    else:
        array = []
        for i in range(cantidad):
            valor = input(f"Ingrese el elemento {i + 1}: ")
            array.append(valor)

        invertido = invertir_array(array)

        print("\nArray original:", array)
        print("Array invertido:", invertido)

except ValueError:
    print("Debe ingresar un número entero válido.")