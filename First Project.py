""""
DATA: 18/03/2021
Projeto: Vamos conhecer agora as especificações do nosso joguinho de adivinhação de
números. As regras são bastante simples. Vamos a elas:
- O jogador deverá escolher um número inteiro qualquer entre 0 e 50;
- O jogador receberá dicas se seu chute está acima ou abaixo do valor oculto
gerado pelo computador de maneira aleatória, caso não acerte de primeira o
número;
- O jogador terá 10 tentativas para adivinhar qual foi o número oculto gerado
pelo computador entre o intervalo (0 a 50).
- Informe ao jogador o no de tentativas feitas e quantas tentativas ainda restam
para ele.
"""" 

x = random.randint(0, 50)
tentativas = 0

while tentativas < 10:
    a = int(input('Vamos lá! Digite um valor: '))
    if a > x:
      print('-> É um número menor! ')
    if a < x:
      print('-> um número maior! ')
    if a == x:
      print('Número correto!')
      break
    tentativas+=1
    print('Tentativas Realizadas: ',(tentativas))
    print('Tentativas Faltantes: ', (10 - tentativas))
break
