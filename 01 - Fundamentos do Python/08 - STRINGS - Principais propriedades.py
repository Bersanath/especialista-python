'''

'''

texto1 = 'EDUARDO PEDRO JORGE TECACUNDA'
texto = 'eduardo pedro jorge tecacunda'

# Método capitalize()
print(texto1.capitalize()) # O método capitalize() ele deixa apenas a primeira letra Maiúscula
print(texto.capitalize())

print('\n')

# Método title()
print(texto1.title()) # O método title() deixa apenas as iniciais em Maiúscula
print(texto.title())

print('\n')

# Método upper()
print(texto1.upper()) # O método upper() deixa a string inteira em Maiúscula 
print(texto.upper()) 

print('\n')

# Método lower()
print(texto1.lower()) # O método lower() deixa a string inteira em Minúscula
print(texto.lower())

print('\n')

# Método center()
print(texto1.center(100,'*')) # O método center() deixa a string centralizada, temos que levar em conta que devemos sempre passar um argumento de tamanho que que queremos centralizar
print(texto.center(100,'-'))

print('\n')

# Método count()
print(texto.count('a')) # O método count() nos permite saber quantas vezes um caracter apareceu em uma string, obs: o count() também diferencia uma letra maiúscula (A) de uma letra minúscula (a)

print('\n')

# Método startswithe()
print(texto1.startswith('EDUARDO')) # O método startswith() verifica se dentro de uma determinada string inicia com um nome específico, ele apenas retorna valor booleanos True ou False

print('\n')

# Método endwith()
print(texto.endswith('a')) # O método endwith() verifica se uma string termina com uma cadeia de caracter

print('\n')

# Método find()
print(texto.find('p')) # O método find() retorna a posição de um determinado valor ou caracter, obs: ele só retorna a primeira ocorrencia

print('\n')

# Método index()
print(texto.index('e')) # O método index() retorna o índice de um determinado valor ou caracter

print('\n')

# Método replece()
print(texto.replace('e','@')) # O método replece() nos permite substituir um valor ou um caracter

print('\n')

# Método isalpha()
print(texto.isalpha()) # O método isalpha() verifica se são caracteres

print('\n')

# Método isalnum()
print(texto.isalnum()) # O método isalnum() verifica se são números

print('\n')

# Método join()
print('_'.join(texto)) # O método join() nos permite juntar uma string

# Método split()
print(texto.split('_'))

# Método strip()
centralizado = texto.center(100)
print(centralizado.strip()) 