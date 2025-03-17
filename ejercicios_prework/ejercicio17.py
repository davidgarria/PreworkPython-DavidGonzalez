# Conversor de Millas a Kilómetros: Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.

def conversor(millas):
  return millas * 1.60934

millas = float(input('Coloque distancia en millas: '))
km = conversor(millas)

print(f'{millas} millas es igual a {km} kilómetros')