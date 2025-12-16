'''
Em Python, finally é uma cláusula usada dentro de blocos try...except para garantir que um código de "limpeza" (como fechar um arquivo ou liberar um recurso) seja sempre executado, independentemente de ter ocorrido um erro (exceção) ou não, sendo essencial para gerenciar recursos de forma segura em qualquer cenário, mesmo com break, continue ou return

Como funciona o finally em Python:
    Sempre executa: O código dentro do finally roda depois do try e do except (se houver), mas antes da saída do bloco try/except.

    Liberação de recursos: É o local ideal para fechar arquivos, conexões de banco de dados ou outras operações que precisam ser desfeitas, evitando vazamentos de recursos.

    Independente de erros: Mesmo que uma exceção ocorra e seja tratada, ou se você sair com return, break ou continue, o finally será executado primeiro, garante Python documentation. 

'''
a = 1
try:
    print(a)
except NameError:
    print('Váriavel não definida')
else:
    print('Quando nenhum erro é levantado')
finally:
    print('Executa Sempre')