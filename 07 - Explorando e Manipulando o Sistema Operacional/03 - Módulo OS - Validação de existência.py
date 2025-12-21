'''
Para validar a existência de um arquivo ou diretório em Python usando o módulo os, você utiliza principalmente os.path.exists(caminho), que retorna True se o caminho existir e False caso contrário, sendo uma função fundamental do submódulo os.path para interagir com o sistema operacional e verificar a presença de itens no sistema de arquivos

'''

import os

print(os.path.exists('path/path2'))
print(os.path.exists('README.md'))
print(os.path.exists('../Testando o os.py'))
print(os.path.getsize('README.md')/ 1e6)
print(os.path.isfile('README.md')) 