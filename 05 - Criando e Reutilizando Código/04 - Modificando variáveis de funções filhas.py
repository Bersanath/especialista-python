'''
Para modificar variáveis em funções "filhas" (ou funções aninhadas/métodos de classes) em Python, você pode passar a variável como argumento, retorná-la, usar a palavra-chave global para variáveis globais, ou usar nonlocal para variáveis em escopo de função pai (closure), e acessar/modificar atributos de objetos self em classes. A escolha depende se a variável é global, de um escopo pai ou de um objeto. 

'''

def calculadora(x,y):
    soma_var = 0
    sub_var = 0

    def soma():
        nonlocal soma_var
        soma_var = x + y
    def sub():
        nonlocal sub_var
        sub_var = x - y
    soma()
    sub()
    print(soma_var)
    print(sub_var)

calculadora(3,2)