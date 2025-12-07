'''
O for em Python é uma estrutura de repetição (loop) que permite iterar sobre sequências (listas, tuplas, strings, etc.), executando um bloco de código "para cada item" dessa sequência, como em "para cada produto em minha lista, faça X". É flexível e funciona como um "for each", sendo ideal para quando você sabe o número de repetições, percorrendo cada elemento de um conjunto de dados. 

'''

lista = [1,2,3,4,'a','b','c']
for x in lista:
    print(x)

print('-'*10)

frutas = ['maça','banana','pera','uva','ananas']
for fruta in frutas:
    print(fruta)

print('-'*10)

dicionario = {'nome': 'Eduardo Pedro', 1: [1,2,3,4], 3: 5+3j}
for elementos in dicionario.items():
    print(elementos)
else:
    print('Fim do laço for!')