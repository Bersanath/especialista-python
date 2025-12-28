'''
    Tudo em python é um objeto
Class é um construtor de objetos

Objetos class suportam dois tipos de operações:referência a atributos e instanciação

Para fazer uma referências a atributos utilizamos a sintaxe padrão da linguagem, colocando o nome do objeto primeiro, um ponto e o nome do atributo que queremos acessar.
'''

class Coordenadas:
    x = 1
    y = 2 # Atributos

    def __init__(self, x,y): # Método
        self.x = x
        self.y = y

instancia = Coordenadas(x = 3, y = 10) # Instância
print(instancia.y)
print(instancia.x)