# Verificación de Año Bisiesto: Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.

def es_bisiesto(anio):
  if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    return True
  return False

anio = int(input('Introduce año: '))

if es_bisiesto(anio):
  print(f'El {anio} es año bisiesto.')
else:
  print(f'El {anio} no es año bisiesto')