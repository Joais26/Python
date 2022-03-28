'''
    Faça um Programa que leia um vetor de 10 números reais e mais-os na ordem inversa.
'''

vetor = []
for x in range(1, 11):
    n = float(input(f'Digite o {x}º número: '))
    print('='*32)
    vetor.append(n)
print(f'Números lidos:')
print(vetor)
print('='*32)
print(f'Numeros inverso:')
print(vetor[::-1])
print('='*32)