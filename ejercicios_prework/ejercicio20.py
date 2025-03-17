# Suma de Números en una Lista: Crea un programa que sume todos los números en una lista ingresada por el usuario.

def suma(lista):
  suma = 0
  for num in lista:
    suma += num
  return suma

numeros = list(map(int, input('Introduce una lista de numeros separados por espacios: ').split()))
resultado = suma(numeros)

print(f'La suma de los numeros de la lista es: {resultado}')