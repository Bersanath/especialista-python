'''
Os blocos try e except em Python são usados para tratar exceções (erros em tempo de execução) e prevenir que o programa trave inesperadamente. Eles permitem que você teste um bloco de código quanto a erros e, se ocorrer um erro, execute um código alternativo para lidar com a situação de forma elegante. 

Como funcionam try, except, else e finally

A estrutura completa do tratamento de exceções em Python envolve quatro blocos principais: 

    try: Contém o código que você suspeita que possa causar um erro (uma exceção).
    except: Este bloco é executado se ocorrer um erro dentro do bloco try que corresponda ao tipo de exceção especificado.
    else: Opcional, este bloco é executado somente se o código no bloco try for concluído sem NENHUM erro.
    finally: Opcional, este bloco é sempre executado, independentemente de ter ocorrido uma exceção ou não. É ideal para tarefas de limpeza, como fechar arquivos ou conexões de rede. 

'''

a = 1
b = 0

try:
    a / b
    print(a)
except ZeroDivisionError:
    print('Não é permitido dividir por Zero')
except NameError:
    print('A váriavel não definida')
except:
    print('Outro ERRO!')