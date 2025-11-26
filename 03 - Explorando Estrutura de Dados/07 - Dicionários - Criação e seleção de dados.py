'''
    O dicionario é uma coleção de dados que nós podemos criar chaves personalizados para os nossos dados que estão armazenados dentro dele, nós conseguimos dar um nome, diferente das listas e tuplas que podemos acessar por intermédio de índice no dicionario nós criamos as chaves e passamos os valores para cada chave criada

    Método do Dicionario:

    1ª keys() Vai retornar as nossas chaves que criamos no nosso dicionario
    2ª values() Vai retornar os valores do nosso dicionario
    3ª items() Vai retornar o conjunto completos as nossas chaves e valores
'''

dicionario = {0: 1, 1: 2, 'nome': 'Eduardo',}
dicionario[3] = 10
print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
