# Calculadora de Descuento: Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

def aplicar_descuento(precio):
  descuento = precio * 0.2
  return precio - descuento

precio = float(input('Coloca el precio al que se le aplicará el descuento: '))
total = aplicar_descuento(precio)

print(f'El total a pagar con el 20% de descuento es: {total}')