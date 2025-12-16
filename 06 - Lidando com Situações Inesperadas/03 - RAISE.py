'''
Em Python, o comando raise é usado para forçar a ocorrência de uma exceção (um erro) em um ponto específico do programa. Isso interrompe o fluxo normal de execução e permite que você sinalize que uma condição inadequada ou um erro ocorreu. 

'''

try:

    raise NameError('Tentando dividir por zero')
except ZeroDivisionError:
    print('ERRO!')
except:
    print('Uma exceção foi levantada')