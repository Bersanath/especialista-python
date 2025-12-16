'''
Para capturar a instância de um erro (exceção) em Python, use o bloco try...except e atribua a exceção a uma variável com a palavra-chave as, permitindo inspecionar detalhes como a mensagem de erro ou o tipo, usando except <TipoDeErro> as e: para obter a instância e do erro, sendo a forma mais comum de tratamento estruturado de exceções em Python. 


'''

# Estrutura Básica

try:

    resultado = 10 / 0

except ZeroDivisionError as e:
    print('Divisão por zero não é permitido')

    print(type(e))
    print(e.args)
    print(e)

'''
Pontos Chave
    try: Contém o código que você suspeita que pode falhar.
    except <TipoDeErro> as e: Captura o erro específico (ex: ZeroDivisionError, ValueError, TypeError) e armazena a instância do erro na variável e.
    as e: É crucial para obter a instância do erro, que contém a mensagem e o tipo.
    Múltiplas exceções: Você pode capturar vários tipos em uma tupla: except (TypeError, ValueError) as e:.
    finally: Código que sempre será executado, com ou sem erro.
    else: Código que roda apenas se o bloco try for concluído sem exceções. 
'''

# Exemplo Prático

try:
    num = int(input('Digite um número: '))
    resultado = 10 / num

except ValueError:
    print('Valor inválido, por favor digite um número inteiro!')
except ZeroDivisionError:
    print('Divsão por zero não é permitido')
except Exception as erro_geral:
    print(f'Um erro inesperado ocorreu: {erro_geral}')
    print(f'Detalhe: {erro_geral.args}')
else:
    print(f'Resultado: {resultado}')

# Ao usar as e, você transforma o tratamento de erros de uma simples interrupção para uma ferramenta poderosa de depuração e log, permitindo inspecionar a exceção capturada. 