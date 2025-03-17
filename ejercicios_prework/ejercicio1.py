# Conversor de Temperatura: Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit

def celsius_a_fahrenheit(celsius): #Funcion que transforma celsius a fahrenheit
  fahrenheit = celsius * 9/5 + 32
  return fahrenheit

temperatura_en_celsius = float(input('Introduzca temperatura en grados Celcius: ')) #Solicitamos temperatura en celsius
resultado = celsius_a_fahrenheit(temperatura_en_celsius) #Llamamos a la función

print(f'{temperatura_en_celsius} grados Celsius equivalen a {resultado} grados Fahrenheit')