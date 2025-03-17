# Calculadora Simple: Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.

def calculadora(operacion, num1, num2):
  if operacion == 'suma':
    return num1 + num2
  elif operacion == 'resta':
    return num1 - num2
  elif operacion == 'multiplicacion':
    return num1 * num2
  elif operacion == 'division':
    if num2 != 0:
      return num1 / num2
    else:
      return 'Error: no se puede dividir por cero'
  else:
    return 'Operacion no valida'

operacion = input('Ingrese la operacion que quiere realizar (suma, resta, multiplicacion o division): ')
num1 = float(input('Ingrese el primer numero a operar: '))
num2 = float(input('Ingrese el segundo numero a operar: '))

solucion = calculadora(operacion, num1, num2)
print(f'El resultado de la {operacion} es: {solucion}')