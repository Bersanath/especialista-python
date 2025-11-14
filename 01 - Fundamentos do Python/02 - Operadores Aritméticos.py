# Os operadores aritméticos são utilizados para fazer operações matemático como: somar (+), dividir na divisão usamos dois tipos de divisão que é (%) o módulo da divisão ou seja o resto da divisão , (/) que é a divisão normal e a divisão inteira (//), para multiplicar usamos o (*) e subtração (-), também temos a exponenciação (**)

'''
ORDEM DE PRECEDÊNCIA

1ª - Parênteses ()
2ª - Potenciação **
3ª - Multiplicação, Divisão e Módulo *, /, %
4ª - Adição e Subtração +, -
'''

numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
print(f'Soma: {soma}')

multiplicar = numero_1 * numero_2
print(f'Multiplicação: {multiplicar}')

divisao_inteira = numero_1 // numero_2
print(f'Divisão Inteira: {divisao_inteira}')

divisao = numero_1 / numero_2
print(f'Divisão: {divisao}')

modulo_divisao = numero_1 % numero_2
print(f'Módulo da Divisão: {modulo_divisao}')

subtrair = numero_1 - numero_2
print(f'Subtração: {subtrair}')

exponenciacao = numero_1 ** numero_2
print(f'Exponenciação: {exponenciacao}')

