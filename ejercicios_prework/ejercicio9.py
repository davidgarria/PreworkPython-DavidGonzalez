# Conversor de Divisas: Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros

def conversor(dolar):
  euros = dolar * 0.85
  return euros

solicitud_dolar = float(input('Por favor, indique la cantidad de dolares que desea cambiar: '))
cambio = conversor(solicitud_dolar)

print(f'{solicitud_dolar} dolares equivalen a {cambio} euros')