'''
Faça um Programa que leia um vetor de 10 caracteres, e diga
quantas foram lidas.
Imprima as correspondentes.
'''

vetor = []
consoantes =  0
vogal = 'aeiou'
for x in range(1, 11):
    letra = input(f'Digite o {x}º caractere: ').lower()    
    if letra not in 'aeiou':
        consoantes += 1
        vetor.append(letra)

print(f'Foram lidas {consoantes} consoantes.')
print(vetor)
