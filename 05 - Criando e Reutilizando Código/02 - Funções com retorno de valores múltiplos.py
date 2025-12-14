'''
Em Python, funções retornam múltiplos valores de forma transparente, empacotando-os automaticamente em uma tupla quando separados por vírgula no return, e permitindo o desempacotamento direto em variáveis separadas na chamada da função, como a, b = minha_funcao(), o que é uma forma elegante de retornar e atribuir vários resultados simultaneamente, ou retornando outras estruturas como listas ou dicionários. 


'''

def calculadora(x,y):
    return x + y, x - y, x * y, x / y

soma,sub,mult,div = calculadora(3,4)


print(soma)