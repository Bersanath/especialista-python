'''
    Hoje faleremos sobre a lista, lista é um tipo de dados que nos permiti a dicionar varios tipos de dados em um único lugar, uma lista pode se inicializar de duas formas, como uma lista vazia e outra com os conteudos já adicionado, uma lista é mútavel ou seja podemos podemos modificar a nossa lista e também criarmos uma lista usamos os parenteses retos []

    Podemos adicionar elementos na lista de 3 maneiras:

    1ª Podemos ultilzar o Método append(): Que nos permite adicionar um elemento no final da lista
    2ª Podemos utilizar o Método insert(): Que nos permite adicionar um elemento na posição dejeada
    3ª Podemos utilizar o Método extend(): Que nos permite unir duas listas em uma única lista
'''

lista = ['Eduardo',1,2,3,4,4.3,2.4] # Aqui fizemos uma lista com os elementos já adicionados
lista2 = [1,55,33,6]
lista.append(49)
lista.insert(1,'entrei aqui')
lista2.extend(lista)

print(lista)
print(lista2)