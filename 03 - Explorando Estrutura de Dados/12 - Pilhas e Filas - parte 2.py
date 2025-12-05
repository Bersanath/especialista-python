'''
Em Python, Pilha (Stack) segue o princípio LIFO (Last In, First Out), usando listas com append() para adicionar e pop() para remover do topo; enquanto Fila (Queue) segue o princípio FIFO (First In, First Out), adicionando no final e removendo do início, geralmente implementada com collections.deque ou listas (embora deque seja mais eficiente para filas). 
Pilha (Stack) em Python (LIFO)

Princípio: O último item adicionado é o primeiro a ser removido (como uma pilha de pratos).
Implementação com Lista:
    Adicionar: minha_pilha.append('item').
    Remover: item_removido = minha_pilha.pop() (remove o último item).
    Verificar Vazio: if not minha_pilha

Fila (Queue) em Python (FIFO)
Princípio: O primeiro item adicionado é o primeiro a ser removido (como uma fila de pessoas).
Implementação Eficiente (collections.deque):
    Adicionar (final): minha_fila.append('item')
    Remover (início): item_removido = minha_fila.popleft()
    Importar: from collections import deque 
'''

pilha = [1,2,3,4]
pilha.append(5) # Ultimo a entrar
print(pilha)
pilha.pop() # é primeiro a sair
print(pilha)

from collections import deque

fila = deque(['Curso','de'])
print(fila)
fila.append('Python')
print(fila)
fila.popleft()
print(fila)