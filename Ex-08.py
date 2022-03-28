'''
 Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idade = []
altura = []
for x in range(1, 6):
    ida = int(input(f'Digite a idade da {x}ª pessoa: '))
    alt = float(input(f'Digite a altura da {x}ª pessoa: '))
    print('='*30)
    idade.append(ida)
    altura.append(alt)

print('Ordem lida')
print('Idade')
print(idade)
print('Altura')
print(altura)
print('='*30)
print('Ordem inversa')
print('Idade')
print(idade[::-1])
print('Altura')
print(altura[::-1])