'''
O módulo os em Python serve para interagir com o sistema operacional, permitindo manipular diretórios e caminhos (usando os.path, os.listdir) e obter metadados de arquivos, mas para ler o conteúdo dos arquivos (dados), você usa funções nativas do Python como open() e seus métodos (ex: .read(), .readlines()), que são a forma padrão de acessar dados de texto ou binários, enquanto os foca na estrutura do sistema de arquivos. Para tipos específicos, use módulos como csv, json ou pandas. 

'''

import os

print(os.stat('README.md'))