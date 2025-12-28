'''
Classes em Python são modelos (blueprints) para criar objetos, que agrupam dados (atributos) e comportamentos (métodos) num só lugar, facilitando código modular e reutilizável, seguindo os princípios da Programação Orientada a Objetos (POO). Você as define com class, usa __init__ para inicializar os atributos com self, e cria objetos (instâncias) que compartilham a estrutura, mas têm dados únicos. 

'''


'''
    Uma classe associa dados(atributos) e operações(métodos) numa só estrutura.

    Um método é uma função que "pertence" a um objeto instância
'''
class MinhaClasse:
    numero = 123 # Atribuito

    def foo(self): # Método
        print('Olá mundo!')

# x = MinhaClasse() # Criando um objeto(intância)

class Cachorro():
    
    def __init__(self,nome,idade):
        self.idade = idade
        self.nome = nome

    def ir_dormir(self):
        print('O cachorro foi dormir!')
nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))

cao = Cachorro(nome,idade)

print(f'O nome do cão: {cao.nome} e a idade do cão: {cao.idade}')

cao.ir_dormir()