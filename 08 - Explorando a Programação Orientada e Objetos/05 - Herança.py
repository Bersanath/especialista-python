'''
Docstring for 08 - Explorando a Programação Orientada e Objetos.05 - Herança

Herança em Python é um conceito de Programação Orientada a Objetos (POO) onde uma classe (filha/subclasse) herda atributos e métodos de outra classe (pai/superclasse), promovendo a reutilização de código e a criação de hierarquias. Existem tipos como Herança Única (uma classe herda de uma só) e Múltipla (uma classe herda de várias), além de multinível e hierárquica, e usa-se super() para acessar métodos da classe pai. 

Conceitos Fundamentais:

    Classe Pai (Superclasse/Base): A classe original que contém os atributos e métodos.

    Classe Filha (Subclasse/Derivada): A nova classe que herda da classe pai, podendo adicionar ou sobrescrever funcionalidades.

    Reutilização de Código: Evita repetir código, pois a filha já tem o que a pai tem. 

Tipos de Herança:

    Herança Simples (Única): Uma classe filha herda de apenas uma classe pai, como class Cachorro(Animal):.

    Herança Múltipla: Uma classe filha herda de duas ou mais classes pai, combinando características de várias.

    Herança Multinível: Uma classe herda de uma classe que, por sua vez, já é uma classe filha, formando uma cadeia (ex: A -> B -> C).

    Herança Hierárquica: Várias classes filhas herdam da mesma classe pai (ex: Cachorro(Animal), Gato(Animal)).

    Herança Híbrida: Combinação de diferentes tipos de herança. 
'''
class Animal:
    def __init__(self, genero,nome):
        self.genero = genero
        self.nome = nome
    def ir_dormir(self):
        print('O animal foi dormir')
    def ir_comer(self):
        print('O animal foi comer')

class Cachorro(Animal):
    def __init__(self, genero,nome):
        super().__init__(genero,nome)
    
    def latir(self):
        print('Au au au')

class Gato(Animal):
    def __init__(self, genero,nome):
        super().__init__(genero,nome)

    def miar(self):
        print('Miau')
    
pingo = Cachorro(genero= 'Macho', nome= 'Pingo')
pingo.ir_comer()
pingo.ir_dormir()
pingo.latir()
print(pingo.nome)

mel = Gato(genero='Femea', nome='Mel')
