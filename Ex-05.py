'''
 Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''

vetorpar  = []
vetorimpar = []
for x in range(1, 21):
    n = int(input(f'Digite o {x}º número: '))
    if n % 2 == 0:
        vetorpar.append(n)
    else:
        vetorimpar.append(n)
print('='*30)
print('Números Pares:')
print(vetorpar)
print('='*30)
print('Números Impares:')
print(vetorimpar)