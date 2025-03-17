# Conversor de Tiempo: Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.

def convertir_tiempo(minutos):
  horas = minutos // 60
  minutos_restantes = minutos % 60
  return horas, minutos_restantes

minutos_totales = int(input("Ingresa la cantidad total de minutos: "))

horas, minutos_restantes = convertir_tiempo(minutos_totales)

print(f'{minutos_totales} minutos serían {horas} horas y {minutos_restantes} minutos')