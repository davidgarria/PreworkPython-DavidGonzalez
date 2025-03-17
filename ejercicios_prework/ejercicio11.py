# Calculadora de Edad: Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

def buscar_edad(anho):
  edad = 2024 - anho
  return edad

anho_nacimiento = int(input('Por favor, indique su año de nacimiento: '))
edad = buscar_edad(anho_nacimiento)

print(f'Si nació en {anho_nacimiento} ahora tiene {edad} años de edad')