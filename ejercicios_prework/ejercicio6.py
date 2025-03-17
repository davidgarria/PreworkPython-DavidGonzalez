#  Verificación de Palíndromo: Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def palindromo(palabra):
  palabra_limpia = palabra.replace(" ","").lower()
  if palabra_limpia == palabra_limpia[::-1]: 
    return 'Es un palindromo'
  else: 
    return 'No es un palindromo'

solicitud_palabra  = input('Por favor, introduzca una plabra/frase: ')
resultado = palindromo(solicitud_palabra)

print(f'{resultado}')