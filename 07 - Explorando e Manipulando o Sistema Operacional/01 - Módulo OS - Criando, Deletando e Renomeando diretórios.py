'''
O módulo os em Python permite gerenciar diretórios com funções como os.mkdir() para criar, os.rmdir() para apagar diretórios vazios e os.rename() para renomear, além de os.makedirs() para criar diretórios e pais e shutil.rmtree() para remover diretórios e seu conteúdo, facilitando a interação com o sistema operacional para manipulação de pastas. 

'''

'''
    1. Criando Diretórios

        os.mkdir(nome_diretorio): Cria um único diretório. Se o diretório pai não existir, um erro é gerado.

        os.makedirs(caminho/completo/diretorio): Cria diretórios e todos os diretórios pais necessários no caminho, como os.makedirs('pasta/subpasta'). 
'''

import os

# Cria um diretório simples
os.mkdir('Path')

# Cria diretórios aninhados
os.makedirs('path2/path3')

'''
    2. Deletando Diretórios

        os.rmdir(nome_diretorio): Remove um diretório vazio. Se o diretório contiver arquivos ou outras pastas, um erro será lançado.

        shutil.rmtree(nome_diretorio): Para deletar um diretório e todo o seu conteúdo (arquivos e subdiretórios), use o módulo shutil (que precisa ser importado).
'''

os.rmdir('path')

os.removedirs('path2/path3')

os.remove('Test2.py') # Removendo arquivo

'''
    3. Renomeando Diretórios (e Arquivos)
        os.rename(origem, destino): Renomeia um diretório ou arquivo, movendo-o para um novo nome ou local.

'''

os.rename('test.py','Test2.py')