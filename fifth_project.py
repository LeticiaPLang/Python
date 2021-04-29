"""
Data: 29/04/2021

Desafio: Criar um programa que auxilie na avaliação de mouses estragados e retorne uma tabela com situação, quantidade e percentual. 

>> sem registro em coleções.

"""


import sys

# definição das variáveis
contador_total = 0
contador_def_1 = 0
contador_def_2 = 0
contador_def_3 = 0
contador_def_4 = 0

# Entrada de dados com tratamento de erros
try:
  identificador = int(input('Digite o código do mouse: '))
  if identificador == 0:
    sys.exit('Saída realizada com sucesso.')
except ValueError:
  print('Insira apenas números inteiros')
  sys.exit('Tente Novamente')

# Processamento com tratamento de erros
while identificador != '0':
  defeito = int(input('1) Necessidade de Esfera;\n2) Necessidade de Limpeza; \n3) Necessidade de Troca de Cabo ou Conector; \n4) Mouse Quebrado ou Inutilizado. \nDigite o defeito encontrado: '))
  if defeito == 1:
    contador_def_1 += 1
  elif defeito == 2:
    contador_def_2 += 1
  elif defeito == 3:
    contador_def_3 += 1
  elif defeito == 4:
    contador_def_4 += 1
  else:
    print('Por favor, escolha uma das 4 opções citadas.')
    break
  print(f'    Registro realizado com sucesso.')
  contador_total += 1
  identificador = input('Digite o código do mouse ou 0 para sair: ')

try:
  perc_1, perc_2, perc_3, perc_4 = contador_def_1/contador_total*100, contador_def_2/contador_total*100, contador_def_3/contador_total*100, contador_def_4/contador_total*100
except ZeroDivisionError:
  print('Nenhum dado foi computado.')
  sys.exit('Por favor, tente novamente.')


#Saída
print('Situação                                       Quantidade       Percentual(%)')
print(f'Necessidade de esfera:                             {contador_def_1}               {perc_1:.1f}')
print(f'Necessidade de limpeza:                            {contador_def_2}               {perc_2:.1f}')
print(f'Necessidade de troca de cabo ou conector:          {contador_def_3}               {perc_3:.1f}')
print(f'Mouse quebrado ou inutilizado:                     {contador_def_4}               {perc_4:.1f}') 
