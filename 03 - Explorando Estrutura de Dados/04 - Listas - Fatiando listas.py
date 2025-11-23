'''
    Fatiando lista, praticamente fazer um fatiamento de uma lista é o mesmo que fazemos no fatiamento de uma string
'''

lista = [10,20,30,40,50,60,70,80,90,100]

print(lista)

# Usando essa duas maneira de fazer cópia de uma lista nos ajuda quando formos alterar a nossa cópia e não vai afetar a lista original

reverso = lista[:] # Essa maneira nos permite fazer uma cópia da nossa lista sem alterar a nossa lista principal
reverso2 = lista.copy() # Esse método também nos possiblita fazer uma cópia de uma lista
reverso.reverse() # O método reverse() é usada para reverter uma lista
print(reverso)