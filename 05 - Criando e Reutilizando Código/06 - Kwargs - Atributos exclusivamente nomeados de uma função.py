'''
**kwargs em Python permite que uma função receba um número variável de argumentos nomeados (chave-valor), empacotando-os em um dicionário dentro da função, o que oferece grande flexibilidade para passar parâmetros adicionais sem alterar a assinatura da função, ideal para configurações extras ou atributos opcionais, como telefone/e-mail de um cliente ou características de um produto. 
Como Funciona:

Sintaxe: Usa-se **kwargs (ou qualquer outro nome após os dois asteriscos) como parâmetro na definição da função, como em def minha_funcao(**kwargs):.
Passagem de Argumentos: Ao chamar a função, você passa os argumentos no formato nome_da_chave=valor, como minha_funcao(nome='Alice', idade=30).
Dentro da Função: kwargs se torna um dicionário (ex: {'nome': 'Alice', 'idade': 30}) que pode ser iterado ou acessado para usar as chaves e valores. 

Por Que Usar:
    Flexibilidade: Adiciona parâmetros dinamicamente sem mudar a função.
    Legibilidade: Mantém o código limpo ao agrupar atributos relacionados.
    Padrão: Útil para funções que precisam de configurações variadas, como construtores de classes (em __init__) ou para passar opções para outras funções.

'''

def func(**kwargs):
    print(kwargs['nome'], kwargs['nacionalidade'])

func(nome = 'Eduardo', nacionalidade = 'Angolana')

def fun(**kwargs):
    print(kwargs.get('nome','fulano'), kwargs.get('nacionalidade')) # O get() é um método usado para pegar o valor de uma dada chave em um dicionário se a chave estiver no dicionário, caso ela não exista, o método retorna None ou o valor padrão passado por parâmetro.

fun()