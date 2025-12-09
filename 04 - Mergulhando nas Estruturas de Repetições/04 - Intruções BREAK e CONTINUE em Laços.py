'''
No Python, break e continue são comandos para controlar loops (for, while), com break saindo completamente do loop quando uma condição é atendida, e continue pulando a iteração atual e indo para a próxima, sem parar o loop todo, sendo úteis para otimizar e refinar a execução de estruturas de repetição. 


Instrução break
    O que faz: Encerra o loop (for ou while) imediatamente, transferindo o controle para a primeira instrução após o loop.
    Quando usar: Quando você encontra o que precisa e não precisa mais continuar iterando, economizando recursos.
    Exemplo: Sair de um loop de busca assim que o item desejado é encontrado. 

Instrução continue
    O que faz: Interrompe apenas a iteração atual do loop e salta para o início da próxima iteração.
    Quando usar: Para ignorar o processamento de certos itens ou condições dentro do loop, mas continuar com os demais.
    Exemplo: Pular o processamento de números pares em um loop. 
'''



a = 0

while a < 10:
    print(a)

    if a == 5:
        break
    a += 1
    print('-'*10)

print('-'*20)

b = 0

while b < 10:
    if b % 2 == 1:
        b += 1
        continue
    print(b)
    b += 1