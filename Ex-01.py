'''
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
print('='*32)
vetor = []
for x in range(1, 6):
    n = int(input(f'Digite {x}º número: '))
    vetor.append(n)
print('='*32)
print(f'Números digitados foram: {vetor}')
