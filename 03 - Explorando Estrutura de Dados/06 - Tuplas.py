'''
    Tuplas é um tipo de dados que nos permite armazenar varios tipos de dados diferente das lista que pode ser alterado entre outros a tuplas não nos permite fazer isso ou seja as tuplas são imútavel ou não podemos modificar a nossa tupla na hora de execução, um parentese não defini uma tupla mais a vírgula que defini a tupla.

    Também podemos fazer os fatiamento em uma tupla
'''

tupla = (1,23,3.12,'Eduardo',True)
print(tupla)

t = (3) # Se nós observamos este exemplo, o tipo desta váriavel é de tipo (int) inteiro mais se nós colocarmos uma vírgula será uma tupla

print(type(t))

print(tupla[0:])

#tupla[0] = 200 # Se nós rodarmos este exemplo ele dará erro
#print(tupla)

tuplas = 'a','b'
print(tuplas)
var1 = tuplas[0]
var2 = tuplas[1]
print(var1)
print(var2)

var1,var2 = tuplas
