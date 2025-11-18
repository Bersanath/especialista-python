'''
Em Python, os operadores de comparação são == (igual), != (diferente), > (maior), < (menor), >= (maior ou igual) e <= (menor ou igual), que avaliam duas expressões e retornam True ou False. Os operadores lógicos são and (e), or (ou) e not (não), usados para combinar múltiplas expressões booleanas.

Operadores de comparação
== (Igual a): Retorna True se os valores forem iguais. Ex: \(10==10\) é True.
!= (Diferente de): Retorna True se os valores forem diferentes. Ex: \(10!=20\) é True.
> (Maior que): Retorna True se o valor da esquerda for maior que o da direita.
< (Menor que): Retorna True se o valor da esquerda for menor que o da direita.
>= (Maior ou igual a): Retorna True se o valor da esquerda for maior ou igual ao da direita.
<= (Menor ou igual a): Retorna True se o valor da esquerda for menor ou igual ao da direita. 

Operadores lógicos
and (E): Retorna True apenas se ambas as expressões forem True.
or (Ou): Retorna True se pelo menos uma das expressões for True.
not (Não): Inverte o valor booleano de uma expressão (de True para False e vice-versa). 
'''

n1 = 10
n2 = 9
diferente = n1 != n2 # Verifica se 10 é diferente de 9
igual = n1 == n2 # Verifica se 10 é igual a 9
maior = n1 > n2 # Verifica se 10 é maior que 9
menor = n1 < n2 # Verifica se 10 é menor que 9
maior_igual = n1 >= n2 # Verifica se 10 é maior ou igual a 9
menor_igual = n1 <= n2 # Verifica se 10 é menor ou igual a 9


print(f'{n1} != {n2}: {diferente}')
print(f'{n1} == {n2}: {igual}')
print(f'{n1} > {n2}: {maior}')
print(f'{n1} < {n2}: {menor}')
print(f'{n1} <= {n2}: {menor_igual}')
print(f'{n1} >= {n2}: {maior}')
