'''
Encapsulamento em Python é o princípio da Programação Orientada a Objetos (POO) que agrupa dados (atributos) e métodos dentro de uma classe, controlando seu acesso para proteger as informações internas e expor apenas uma interface pública, usando convenções como _ (protegido) e __ (privado) para indicar restrição, e @property/@setter para getters e setters mais pythônicos, permitindo controle refinado sobre a manipulação dos dados.

Como funciona:

    Ocultação de detalhes: Esconde a implementação interna de uma classe, permitindo que o usuário interaja apenas com métodos públicos, como dirigir um carro sem saber como o motor funciona.

    Proteção de dados: Impede o acesso direto e a modificação indevida de atributos sensíveis (como saldo bancário), forçando o uso de métodos controlados para leitura/escrita. 

Convenções em Python:

    _atributo (Protegido): Indica que o atributo não deve ser acessado diretamente fora da classe, mas o Python não impede o acesso (é uma convenção).

    __atributo (Privado): Torna o atributo "privado" por meio de "name mangling" (alteração de nome), dificultando o acesso externo, mas ainda possível com o nome completo _NomeDaClasse__atributo.

    Métodos getter e setter: Usados para controlar o acesso a atributos protegidos/privados.
    Tradicional: get_atributo() e set_atributo(valor).
    Pythônico (@property): Permite usar a sintaxe de atributo (objeto.atributo) com lógica de validação em métodos, como @property para ler e @atributo.setter para escrever. 
'''

class A:
    a = 3
    __b = 5

class B:
    __c = 3

    def __init__(self):
        print(self.__c + 3)

inst = B()
instancia = A()