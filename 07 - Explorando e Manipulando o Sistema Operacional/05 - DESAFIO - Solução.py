'''
    1- Escreva um programa Python para listar apenas diretórios, apenas arquivos, arquivos e todos os diretóriosdo diretório atual(Onde o script estiver a rodando). 
'''

import os

diretorio_atual = os.listdir()
print('Listando apenas os Diretórios')

for elem in diretorio_atual:
    if os.path.isdir(elem):
        print(elem)
print('Listando apenas os Ficheiros')
for elem in diretorio_atual:
    if os.path.isfile(elem):
        print(elem)

print('Listando Arquivos e o Diretórios')
df, * demais = os.walk(os.getcwd())
print(df)

'''
    2- Escreva um programa que cria um arquivo TXT, escreva alguns texto nele e o renomia 
'''

with open('Arquivo.txt', 'w') as file:
    print(file.write('Ola programador'))
print(os.rename(src='Arquivo.txt', dst='Arquivo2.txt'))