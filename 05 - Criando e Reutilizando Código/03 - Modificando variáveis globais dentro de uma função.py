'''
Para modificar uma variável global dentro de uma função Python, você deve usar a palavra-chave global antes do nome da variável, indicando ao interpretador que você se refere à variável do escopo global e não a uma nova variável local com o mesmo nome, o que evita erros e permite a alteração do valor original. Sem global, uma atribuição dentro da função criaria uma variável local, mas o uso de global força a modificação do valor externo. 

'''

comida = 'arroz' # Aqui nós encontramos uma variável global ou seja ele funciona em qualquer parte do código

def func():
    comida = 'batata' # Aqui nós encontramos uma variável local ou seja ele funciona apenas dentro da minha função
    print(comida)

print(comida)
func()