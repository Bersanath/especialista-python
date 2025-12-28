'''
Docstring for 08 - Explorando a Programação Orientada e Objetos.04 - Destrutores

Destrutores em Python são métodos especiais del() que são chamados automaticamente quando um objeto está prestes a ser destruído pelo coletor de lixo (garbage collector), permitindo a execução de código de limpeza para liberar recursos externos não gerenciados pelo Python, como arquivos ou conexões de rede, embora a gestão de memória seja automática. 

Como funcionam:

    Chamada Automática: O método __del__ é invocado pelo coletor de lixo quando um objeto não tem mais referências e será removido da memória.

    Liberação de Recursos: É usado para fechar arquivos, liberar sockets, ou fazer qualquer outra tarefa de "limpeza" necessária antes que o objeto desapareça completamente. 
'''

class Veiculo:
    def __init__(self):
        print('Veiculo criado!')
    
    def __del__(self):
        print('Carro destruido')

carro = Veiculo()
del carro
print(carro)