'''
 Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''


notas = []
for x in range(1, 5):
    n = float(input(f'Digite sua {x}ª nota: '))
    notas.append(n)
    print('='*30)
media = sum(notas) / len(notas)

print(f'A media é {media}')
print('='*30)