"""
Leia a temperatura em graus celsius e apresente-a convertida em graus fahrenheit.

DATA: 26/04/2021
"""
try:
  celsius = float(input('Digite a tempuratura (°C): '))
  print(f'Essa temperatura é {celsius * (9.0/5.0) + 32.0} em Fahrenheit')
except ValueError:
  print('Você precisar inserir um número.')
