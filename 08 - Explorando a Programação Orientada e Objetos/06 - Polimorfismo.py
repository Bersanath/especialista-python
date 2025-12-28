'''
Polimorfismo em Python é a capacidade de diferentes objetos responderem à mesma mensagem (chamada de método) de formas distintas, permitindo código mais flexível e reutilizável, onde uma função pode operar em objetos de classes diferentes, desde que esses objetos compartilhem um método com o mesmo nome, mesmo que não sejam de uma hierarquia de herança explícita (Duck Typing). Ele permite que classes diferentes implementem um método com a mesma assinatura de forma única, como fazer_som() para um Cachorro ("Au au!") e um Gato ("Miau!").
'''

class Animal:
    def __init__(self, genero,nome):
        self.genero = genero
        self.nome = nome
    def ir_dormir(self):
        print('O animal foi dormir')
    def ir_comer(self):
        print('O animal foi comer')

    def __del__(self):
        print('O animal Faleceu')

class Cachorro(Animal):
    def __init__(self, genero,nome):
        super().__init__(genero,nome)
    
    def latir(self):
        print('Au au au')
    def __del__(self):
        print(f'O {self.nome} Faleceu')
class Gato(Animal):
    def __init__(self, genero,nome):
        super().__init__(genero,nome)

    def miar(self):
        print('Miau')
    def __del__(self):
        print(f'O {self.nome} Faleceu')
    
pingo = Cachorro(genero= 'Macho', nome= 'Pingo')
pingo.ir_comer()
pingo.ir_dormir()
pingo.latir()
del pingo
print(pingo.nome)

mel = Gato(genero='Femea', nome='Mel')
