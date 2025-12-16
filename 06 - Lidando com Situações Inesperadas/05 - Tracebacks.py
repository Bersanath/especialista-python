'''
Em Python, um traceback (traço de pilha ou pilha de chamadas) é a mensagem detalhada que o interpretador exibe quando um erro (exceção) ocorre, mostrando a sequência exata de chamadas de funções que levaram ao ponto do erro, incluindo o arquivo, número da linha e o tipo de erro, ajudando o desenvolvedor a identificar e corrigir o problema rapidamente, como uma "história" de onde o código falhou. 

Componentes de um Traceback
    Traceback (most recent call last):: Indica que o traceback está listando as chamadas mais recentes primeiro.
    File "<nome_do_arquivo>", line <numero>, in <funcao>: Mostra o arquivo, linha e função onde a chamada ocorreu.
    ...: Indica que pode haver mais chamadas de função intermediárias.
    NameError: name 'variavel_inexistente' is not defined: O tipo da exceção (ex: NameError, ZeroDivisionError) e uma descrição do erro. 
'''

def funcao_b():
    print(10 / 0) # Isso vai gerar um erro

def funcao_a():
    funcao_b()

funcao_a()

# Traceback gerado:

'''Traceback (most recent call last):
  File "seu_arquivo.py", line 8, in <module>
    funcao_a()
  File "seu_arquivo.py", line 5, in funcao_a
    funcao_b()
  File "seu_arquivo.py", line 2, in funcao_b
    print(10 / 0)
ZeroDivisionError: division by zero
'''

'''

Como Usar
    Leia de baixo para cima: O erro real está na última linha (o tipo de exceção) e o caminho para ele está nas linhas anteriores.
    Localize o arquivo e linha: Encontre o File "<nome_do_arquivo>", line <numero> para saber onde o erro ocorreu.
    Identifique o erro: Verifique a mensagem final (ZeroDivisionError, TypeError, etc.) para entender o problema e corrigi-lo no código. 
'''
