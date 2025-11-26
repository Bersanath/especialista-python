'''

'''

dicionario = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print(4 in dicionario) # O método in ele vai procurar se valor que passamos contem nas chaves do dicionario,ele apenas verifica a chave não o valor

print('a' in dicionario.values()) # desta maneira ele vai procurar o valor dentro do dicionario

dicionario2 = dicionario.copy() # O método copy() nos ajuda fazer uma cópia do nosso dicionario
dicionario2[5] = 'e'
print(dicionario2)
print(dicionario)