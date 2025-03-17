# Cálculo del Índice de Masa Corporal (IMC): Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona. 

def calculo_imc(peso, altura): #Funcion para calcular el IMC y su clasificacion
  imc = peso / (altura ** 2)
  if imc < 18.5:
    clasificacion = 'Bajo peso'
  elif 18.5 <= imc < 24.9:
    clasificacion = 'Peso normal'
  elif 25 <= imc < 29.9:
    clasificacion = 'Sobrepeso'
  else:
    clasificacion = 'Obesidad'
  return imc, clasificacion

solicitud_peso = float(input('Indicar peso en Kg: '))
solicitud_altura = float(input('Indicar altura en metros: '))

imc, clasificacion = calculo_imc(solicitud_peso, solicitud_altura)

print(f'Tu IMC es de: {imc:.2f}')
print(f'Clasificacion: {clasificacion}')

