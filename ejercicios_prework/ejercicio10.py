# Determinar el Día de la Semana: Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

def dia_de_semana(numero):
  semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
  if numero >= 1 and numero <=7:
    return semana[numero -1]

numero_de_dia = int(input('Seleccione el numero del dia de la semana que quiere buscar: '))
dia = dia_de_semana(numero_de_dia)

print(f'El dia de la semana es: {dia}')