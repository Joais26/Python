'''
 Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''
primeiro_vetor = []
segundo_vetor = []
terceiro_vetor = []
quarto_vetor = []
for i in range(10):
    primeiro_vetor.append(input('Digite o '+ str(i + 1) + 'º elemento do primeiro vetor: '))
print('='*50)
for i in range(10):
    segundo_vetor.append(input('Digite o '+ str(i + 1 )+ 'º elemento do segundo vetor: '))
print('='*50)
for i in range(10):
    terceiro_vetor.append(input('Digite o '+ str(i + 1 )+ 'º elemento do terceiro vetor: '))
print('='*50)
for indice in range(10):
    quarto_vetor.append(primeiro_vetor[indice])
    quarto_vetor.append(segundo_vetor[indice])
    quarto_vetor.append(terceiro_vetor[indice])

print(quarto_vetor)