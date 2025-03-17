# Suma de Números Pares: Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

suma = 0

for numeros in range(1,101):
  if numeros % 2 == 0:
    suma += numeros

'''
Otra forma de hacerlo sería:
for numeros in range(12, 101, 2): # el 2 del final indica que es aplica la operacion cada 2 unidades
  suma += numeros
'''

print(f'La cantidad de números pares entre el 1 y el 100 es: {suma}')