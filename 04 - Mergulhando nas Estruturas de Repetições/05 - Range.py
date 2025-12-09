'''
A função range() em Python gera uma sequência imutável de números inteiros, muito usada em loops for para definir quantas vezes um bloco de código deve rodar ou para iterar sobre índices, aceitando até três argumentos: start (início, padrão 0), stop (fim, exclusivo) e step (passo, padrão 1), sendo stop obrigatório e a função retornando um objeto iterável, não uma lista diretamente, o que economiza memória. 
'''

print(list(range(5)))

for element in range(5):
    print(element,end=' ')