'''
A função enumerate() em Python adiciona um contador a um iterável (como listas, tuplas, strings) e retorna um objeto enumerado, que produz pares de (índice, valor) em cada iteração, começando o índice por padrão em 0, sendo ideal para loops for quando se precisa acessar tanto a posição quanto o item simultaneamente, resultando em um código mais limpo e "pythônico". 

Como funciona:

    Sintaxe: enumerate(iterable, start=0).
    iterable: A sequência que você quer percorrer (lista, tupla, string, etc.).
    start (opcional): O valor inicial para o contador (padrão é 0). 


'''

frutas = ['maça','banana','pera','uva','laranja']
for indice, fruta in enumerate(frutas):
    print(f'Índice {indice} -> {fruta} ')