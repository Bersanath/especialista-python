

conjunto1 = {1,2,3,4,5}
conjunto2 = {1,3,5,7}

subconjunto = conjunto1.issubset(conjunto2) # issubset() é um método para verificar se um conjunto está contido em outro (se é um subconjunto), retornando True ou False

superconjunto = {1,2,3}.issuperset({1,2,3}) # issuperset() é um método de conjuntos (set) que verifica se um conjunto é um superconjunto de outro, ou seja, se ele contém todos os elementos de um segundo conjunto

disconjunto = conjunto1.isdisjoint(conjunto2) # isdisjoint() é um método de conjuntos (set) que retorna True se dois conjuntos não possuem elementos em comum (são disjuntos), e False caso haja qualquer elemento compartilhado entre eles, sendo uma forma eficiente de verificar a intersecção de dois conjuntos
print(f'Subconjunto: {subconjunto}')
print(f'Superconjunto: {superconjunto}')
print(f'Disconjunto: {disconjunto}')