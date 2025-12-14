'''
Em Python, argumentos posicionais são passados pela ordem, enquanto argumentos nomeados (ou por palavra-chave) são passados com o nome do parâmetro (ex: nome='Ana'), e *args e **kwargs são usados para funções que aceitam um número variável de argumentos: *args para argumentos posicionais variáveis (como uma tupla) e **kwargs para argumentos nomeados variáveis (como um dicionário), permitindo funções mais flexíveis, com a ordem padrão sendo (posicionais, *args, nomeados, **kwargs). 

Argumentos Posicionais
Definição: O valor é associado ao parâmetro pela posição em que é passado.
Exemplo: def saudacao(nome, sobrenome): ...
Chamada: saudacao("Maria", "Silva") (Maria vai para nome, Silva para sobrenome). 
Argumentos Nomeados (Keyword Arguments)
Definição: Passados usando o nome do parâmetro, a ordem não importa.
Exemplo: def criar_usuario(nome, email): ...
Chamada: criar_usuario(email="a@b.com", nome="Carlos"). 

Argumentos Variáveis
*args (Argumentos Posicionais Variáveis): Permite passar um número indefinido de argumentos posicionais, que são coletados em uma tupla.
Exemplo: def soma(*numeros): ...
Chamada: soma(1, 2, 3, 4) (dentro da função, numeros será (1, 2, 3, 4)).
**kwargs (Keyword Arguments Variáveis): Permite passar um número indefinido de argumentos nomeados, coletados em um dicionário.
Exemplo: def exibir_info(**dados): ...
Chamada: exibir_info(nome="João", idade=30) (dentro da função, dados será {'nome': 'João', 'idade': 30}). 
Ordem Correta em Definições de Função
Parâmetros regulares, *args, parâmetros nomeados (padrão), **kwargs. 

'''

def Soma(*args):
    soma = 0

    for elemet in args:
        soma += elemet
    print(soma)
Soma(1,2,43,12,10)