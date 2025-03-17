# Calculadora de Propina: Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.

total_cuenta = float(input('Ingresa el total de la cuenta: '))

propina = total_cuenta * 0.15

total_a_pagar = total_cuenta + propina

print(f'La propina del 15% es: {propina}')
print(f'El monto total a pagar es: {total_a_pagar:}')