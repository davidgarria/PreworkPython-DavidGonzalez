# Contador de Palabras: Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

def contar_palabras(oracion):
  palabras = oracion.split()
  return len(palabras)

oracion = input('Introduce una oración: ')
numero_palabras = contar_palabras(oracion)

print(f'La oracion tiene {numero_palabras} palabras.')