'''
Faça um Programa que leia um vetor de 5 números inteiros
, mostre a soma,
a multiplicação e os números.
'''

vetor = []
multiplicacao = 1
for x in range(1, 6):
    n = int(input(f'Digite o {x}º Número: '))
    vetor.append(n)

soma = 0
multiplicacao = 1
for n in vetor:
    soma += n
    multiplicacao *= n

print('='*30)
print('Números')
print(vetor)
print('='*30)
print('Soma')
print(f'{soma}')
print('='*30)
print('Multiplicação')
print(f'{multiplicacao}')
