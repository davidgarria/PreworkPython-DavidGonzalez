# Contador de Números Pares e Impares: Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

def contador(numeros):
  par = 0
  impar = 0
  for numero in numeros:
    if numero % 2 == 0:
      par += 1
    else:
      impar += 1
  return par, impar

numeros = list(map(int, input('Coloque una lista de números enteros separados por comas: ').split(',')))
par, impar = contador(numeros)

print(f'Cantidad de números pares: {par}')
print(f'Cantidad de números impares: {impar}')