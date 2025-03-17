# Verificación de Número Primo: Escribe un programa que determine si un número ingresado por el usuario es primo o no.

def es_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
  else:
    return True

num = int(input('Coloca un número para verificar si este es primo: '))

if es_primo(num):
  print(f'{num} es un número primo')
else:
  print(f'{num} no es un número primo')