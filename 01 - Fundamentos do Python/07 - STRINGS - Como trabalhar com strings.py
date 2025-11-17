'''
    Hoje vamos falar sobre strings em Python. Uma string é uma sequência imutável de caracteres, usada para representar texto.

Características principais:

Índices começam em 0

São imutáveis (não podem ser alteradas diretamente)

Suportam operações de fatiamento (slicing)

Fatiamento de strings:
Nos permite acessar partes específicas da string usando a sintaxe [início:fim:passo]

Exemplos:
'''

# Regra importante: No fatiamento [início:fim], o índice de início é incluído e o índice de fim é excluído!

palavra = 'String'

print(palavra[3]) # Isso chama-se fatiamento de strings isso nos ajuda acessar varias parte da nossa string

print(palavra[0:3]) # Aqui nós queremos acessar uma determinada quantidade de caracter que vai do indice 0 até o indice 3 que será: str mais por que até 3 e não 2, normalmente a contagem da string sempre que fazemos o fatiamento ele inclui sempre a esquerda mais nunca a direita  se tivessemos colocado o 2 ele apenas irá apresentar (st) e não (str) por que o último indice será excluido. 

print(palavra[0:]) # Se eu quero fazer o fatiamento de toda a string e eu não até onde vai a minha string é só eu usar (:) ele vai do início até o mais infinito

palavra1 = 'Python'

print(palavra1[2]) # 't' - acesso por índice
print(palavra1[0:3]) # 'Pyt' - do índice 0 ao 2 (o 3 é excluído)
print(palavra1[0:]) # 'Python' - do início até o final
print(palavra1[:3]) # 'Pyt' - do início até o índice 2
print(palavra1[-1]) # 'n' - último caractere (índices negativos)
print(palavra1[::1]) # 'Python' - da passo de 1 em 1 passo
print(palavra1[-1:-6])