'''
Em Python, os Operadores de Identidade (is, is not) verificam se dois objetos são o mesmo objeto na memória, não apenas se têm o mesmo valor, enquanto os Operadores de Associação (in, not in) checam se um valor está presente ou ausente em uma sequência (lista, tupla, string, etc.), retornando True ou False. Eles são úteis para comparações de memória e pertencimento a coleções, respectivamente, e são diferentes dos operadores de igualdade (==) ou comparação. 

Operadores de Identidade
    is: Retorna True se ambas as variáveis apontam para o mesmo objeto na memória.
    is not: Retorna True se as variáveis NÃO apontam para o mesmo objeto na memória.
    Uso: Diferenciar objetos com o mesmo valor, mas que são instâncias distintas (especialmente com objetos mutáveis). 

Operadores de Associação
    in: Retorna True se o valor for encontrado na sequência.
    not in: Retorna True se o valor NÃO for encontrado na sequência.
    Uso: Verificar a presença de elementos em listas, tuplas, strings, dicionários (chaves ou valores) e conjuntos. 


'''

a = 'abc'
b = 'cde'
c = 'abc'

print(a is b)
print(a is not c)

print('a' in 'Eduardo')

print('a' not in 'Eduardo')