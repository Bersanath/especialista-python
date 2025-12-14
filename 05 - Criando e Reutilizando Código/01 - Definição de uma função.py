'''
Funções em Python são blocos de código reutilizáveis e nomeados, definidos com def, que agrupam instruções para realizar tarefas específicas, tornando o código mais organizado, legível e fácil de manter, permitindo a reutilização de lógica e evitando repetições, com capacidade de receber dados (parâmetros/argumentos) e retornar resultados. Elas funcionam como peças de LEGO modulares, essenciais para dividir programas complexos em partes menores e gerenciáveis.

Principais características e benefícios:
    Reutilização de Código: Evitam a necessidade de reescrever o mesmo código várias vezes.
    Modularidade: Dividem o programa em partes menores e focadas em uma única tarefa.
    Organização: Tornam o código mais limpo e fácil de entender.
    Manutenção: Simplificam a depuração e a modificação do código
'''

def foo():

    valor = 1
    print(valor)

foo()

def anfitriao(nome):
    print(f'Olá, {nome} seja muito bem vindo ao Curso de Python')

anfitriao('Eduardo')