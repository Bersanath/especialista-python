'''
Em Python, o construtor é um método especial chamado __init__ que é executado automaticamente ao criar um novo objeto (instância) de uma classe, servindo para inicializar seus atributos com valores iniciais ou definir seu estado básico, usando self como o primeiro parâmetro para referenciar a própria instância. Ele não é obrigatório, mas é essencial para configurar objetos de forma padronizada, recebendo parâmetros que definem as características do objeto, como def __init__(self, nome, idade):. 

Como funciona o __init__

    Chamado Automaticamente: Quando você escreve pessoa = Pessoa("Ana", 25), o __init__ é chamado automaticamente para criar o objeto pessoa, passando "Ana" para nome e 25 para idade.

    self: É uma referência obrigatória ao próprio objeto sendo criado, permitindo que você defina atributos específicos para essa instância (ex: self.nome = nome).
    
    Inicialização de Atributos: É o local ideal para atribuir valores aos atributos da classe, garantindo que todos os objetos criados tenham esses atributos desde o início. 
'''

class Pessoa:

    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
sexo = str(input('Digite o sexo(m/f): ')).lower()

dados = Pessoa(nome,idade,sexo)
print(f'O seu nome: {dados.nome} a sua idade: {dados.idade} e o seu sexo: {dados.sexo}') 