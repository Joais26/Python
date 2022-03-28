'''
 Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''
numeros = []
for x in range(1, 11):
    n = int(input(f'Digite o {x}º número: '))
    numeros.append(n)
print('='*30)
for numero in numeros:
    print(f'{numero}² = {numero ** 2}')