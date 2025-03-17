# Calculadora de Área de un Rectángulo: Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.

def area(longitud, ancho):
  return longitud * ancho

longitud = float(input('Indique la longitud del rectangulo: '))
ancho = float(input('Indique el ancho del rectangulo: '))

area = area(longitud, ancho)
print(f'El area del rectangulo es: {area}')