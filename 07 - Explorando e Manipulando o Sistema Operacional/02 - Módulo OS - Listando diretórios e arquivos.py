'''
    O módulo os em Python permite listar diretórios e arquivos usando os.listdir(caminho), que retorna uma lista de nomes de arquivos e pastas no caminho especificado, e os.path (como os.path.join, os.path.isfile, os.path.isdir) para manipular esses caminhos e identificar se são arquivos ou diretórios, sendo pathlib uma alternativa moderna orientada a objetos para operações de sistema de arquivos. 
'''

import os

print(os.listdir()) # os.listdir(path): Retorna uma lista contendo os nomes de todas as entradas (arquivos e subdiretórios) dentro do path fornecido.

print(os.getcwd()) # os.getcwd() é usado para obter o diretório de trabalho atual (Current Working Directory), ou seja, a pasta onde o seu script Python está sendo executado, e retorna esse caminho como uma string, sendo útil para manipulação de arquivos e caminhos no sistema operacional. 

for dirpath, dirname, filename in os.walk(os.getcwd()): # os.walk() em Python é um gerador que percorre uma árvore de diretórios, retornando tuplas com o diretório atual (root), subdiretórios (dirs) e arquivos (files) em cada nível, sendo ótimo para navegar e processar arquivos e pastas de forma recursiva, como para buscar/listar todos os arquivos em um diretório e seus subdiretórios em Python
    for diretorio in dirname:
        print('-',diretorio)
    for file in filename:
        print('--',file)
