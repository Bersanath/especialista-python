'''
    Hoje vamos aprender a remover um elemento dentro da nasso lista, assim como podemos adicionar um elemento também podemos remover um elemento

    1ª Método pop(): utilizando o método pop() podemos remover o ultimo elemento da nossa lista, mais se nós passarmos um parametro ele vai eliminar aquelas posição que passamos

    2ª Método remove(): podemos remover um elemento na lista passando seu nome, diferente do pop que deemos remover no final ou se passamos o índice que queremos remover o remove() ele apenas remove se nós passarmos um dos nomes da nossa lista

    3ª Método clear(): este método nos permite apagar todos os elementos da nossa lista
'''

lista = [1,2,3,'Eduardo',1.2,1.8,True]
lista[2] = 45 # Aqui estamos a altar o valor de uma lista por outro valor

lista.pop(1)
lista.remove('Eduardo')
lista.clear()
print(lista)