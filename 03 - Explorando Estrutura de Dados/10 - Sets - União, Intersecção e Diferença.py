'''

'''

conjunto1 = {1,2,3,4}
conjunto2 = {'a','b','c','d'}
uniao = conjunto1.union(conjunto2) # O método union() nos ajuda a unir dois sets
print(uniao)

conjunto3 = conjunto1.intersection({1,4,5,29}) # o método intersection() ele procura a interseção dos dois conjutos
print(conjunto3)

conjunto4 = {1,2,3,4,5,6,7}
conjunto5 = {1,5,7,9}

diferenca = conjunto4.difference(conjunto5) # O método diference() ele nos permite saber a diferença entre dois set()
print(diferenca)

conjunto6 = {1,2,3,4,5,6,7}
conjunto7 = {1,3,5,7,9}

simetrica = conjunto6.symmetric_difference(conjunto7) # o método symmetric_diference() ele nos permite ver a simetria de dois conjuntos
print(simetrica)