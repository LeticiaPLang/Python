  
"""
Data: 29/04/2021
Desafio: desenvolver um algoritmo que carregue um vetor de 5 elementos inteiros e em seguida armazene em um vetor apenas os números pares maiores que zero. 
No final, mostrar os elementos do vetor na tela.
"""

pares = []
num = []
chance = 0

for n in range (5):
  try:
    num = int(input('Digite um número inteiro: '))
    if num > 0 and num % 2 == 0:
      pares.append(num)
  except ValueError:
    chance += 1
    print(f'Você perdeu {chance} chance(s). Por favor, insira apenas números inteiros.')

if pares == []:
  print('Nenhum número par foi inserido.')
else:
  print(f"Os números pares inseridos foram {pares}")
