# Contador de Vocales: Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.

def contar_vocales(palabra):
  vocales = "aeiouAEIOU"
  contador_vocales = 0
  for letra in palabra:
    if letra in vocales:
      contador_vocales += 1
  return contador_vocales

palabra_o_frase = input('Introduzca una palabra o una frase: ')

cantidad_vocales = contar_vocales(palabra_o_frase)

print(f'En la palabra/frase {palabra_o_frase} hay {cantidad_vocales} vocales')