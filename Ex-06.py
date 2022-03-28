'''
 Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
'''

medias = []
for x in range(1, 11):
    soma, media = 0, 0
    for y in range(1, 5):
        n = float(input(f'Digite sua {y}ª notado {x}º Aluno: '))       
        soma += n
    media = soma / 4
    print('='*30)
    medias.append(media)

aluno = cont = 0
for media in medias:
    if media >= 7:
        aluno += 1
    if media < 7:
        cont += 1

print(f'Número de alunos com média maior ou igual a 7: {aluno}')
print(f'Número de alunos com média abaixo de 7: {cont}')