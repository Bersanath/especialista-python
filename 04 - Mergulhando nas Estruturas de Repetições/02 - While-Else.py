'''
Em Python, a estrutura while...else permite executar um bloco de código (else) apenas se o loop while terminar naturalmente, ou seja, sem ser interrompido por uma instrução break. É útil para tarefas como verificar se um loop completou sua execução sem encontrar um critério de saída específico, como em buscas ou validações. 

While é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira, parando apenas quando ela se torna falsa, sendo ideal para repetições de número indeterminado de vezes, usando a palavra-chave while, seguida da condição e do código indentado para repetição, sendo crucial alterar a condição dentro do loop para evitar um loop infinito. 
'''

'''a = 10
b = 0
while a >= 0:
    print(a)
    a -= 1'''
a = 10
b = 0
while a != b:
    print(f'Valor de a: {a}')
    print(f'Valor de b: {b}')
    print('-'*10)

    a -= 1
    b += 1

f = 'Curso de Python'
g = len(f)

while f[:g].startswith('Curso de '):
    print(f[:g])

    g -= 1
else:
    print(f[:g] + ' Django')
