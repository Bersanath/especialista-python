'''
Em Python, um traceback (traço de pilha ou pilha de chamadas) é a mensagem detalhada que o interpretador exibe quando um erro (exceção) ocorre, mostrando a sequência exata de chamadas de funções que levaram ao ponto do erro, incluindo o arquivo, número da linha e o tipo de erro, ajudando o desenvolvedor a identificar e corrigir o problema rapidamente, como uma "história" de onde o código falhou. 

Componentes de um Traceback
    Traceback (most recent call last):: Indica que o traceback está listando as chamadas mais recentes primeiro.
    File "<nome_do_arquivo>", line <numero>, in <funcao>: Mostra o arquivo, linha e função onde a chamada ocorreu.
    ...: Indica que pode haver mais chamadas de função intermediárias.
    NameError: name 'variavel_inexistente' is not defined: O tipo da exceção (ex: NameError, ZeroDivisionError) e uma descrição do erro. 
'''

