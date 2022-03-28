'''
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.
'''
primeiro_vetor = []
segundo_vetor = []
terceiro_vetor = []
for x in range(10):
    primeiro_vetor.append(input('Digite o '+ str(x+1) + 'º elemento do primeiro vetor: '))
print('='*50)
for x in range(10):
    segundo_vetor.append(input('Digite o ' + str(x+1) + 'º elemento do segundo vetor: '))
print('='*50)
for indice in range(10):
    terceiro_vetor.append(primeiro_vetor[indice])
    terceiro_vetor.append(segundo_vetor[indice])
print(terceiro_vetor)