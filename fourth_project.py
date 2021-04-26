"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados deles.
"""
try:
    num1 = int(input('Insira o primeiro valor: '))
    num2 = int(input('Insira o segundo valor: '))
    num3 = int(input('Insira o terceiro valor: '))
    print(num1**2 + num2**2 + num3**2)
except ValueError:
    print('Por favor, insira apenas números.'.)
