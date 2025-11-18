'''
    A estrutura condicional nos permite toma a decisão de uma certa operação, 
'''

x = 10
y = 9

if x > y: # a condição (if) ou se ele verifica se 10 é maior que 9, essa condição só é valida se a nossa condição for verdadeiro
    print(f'{x} é maior que {y}')
else: # Se a nossa condição for false ela cai no bloco (else) que significa se não
    print(f'{y} é maior que {x}')
idade = int(input('Qual a sua idade? '))

if idade >= 25:
    print('Adulto!')
elif idade >= 18:
    print('Jovem')
else:
    print('Você menor de idade!')

# Também podemos avaliar multipla condições no bloco if ou elif