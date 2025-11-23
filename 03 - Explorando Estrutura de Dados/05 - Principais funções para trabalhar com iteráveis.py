'''
    Principais funções com iteráveis:

    Funções:

        1 - len() está função nos permite saber qual é o tamanho da nossa lista
        2 - sorted() está função ordena uma lista como também pode ordenar strings
        3 - sum() está função retorna o somatorio dos elementos de uma lista
        4 - max() está função retorna o maior valor de uma lista
        5 - min() está função retorna o menor valor de uma lista
'''

lista = [1,2,3,6,9,4,3,8,6,9,7,2,5,'eduardo',True,False,2.32,3.56]
print(len(lista)) # A função len() também funciona com string
print(sorted(lista, key=str))

strings = 'Eduardo Pedro jorge Tecacunda'
print(len(strings))

numeros = [1,2,3,4,5,6,7,8,9,10]
print(f'O somatorio é: {sum(numeros)}')

print(f'O maior valor da lista é: {max(numeros)}') # Podemos usar a função max() dentro de uma string
print(f'O menor valor da lista é: {min(numeros)}')  # Podemos usar a função min() dentro de uma string