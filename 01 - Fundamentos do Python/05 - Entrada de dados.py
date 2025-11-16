'''
Hoje vamos falar sobre a entrada de dados, para que aja uma comunicação entre o usuário e o computador ou o sistema nós temos a função input() que em inglês significa entra, está mesmo função nos perminte escrever a parte do teclado o dados que queremos atríbuir em uma variável
'''

nome = input('Qual o seu nome? ') # obs: Tem uma coisa que temos que levar em conta é que devemos sempre especificar o tipo de dados que vamos usar para não se deparar com resultdos diferentes ou com erros

print(nome) # por exemplo nesta saída se na entrar o usuário digitar números ele vai passar e isso não acontecer porque um número não é um texto a não ser que agente faça a conversão

nome = str(input('Qual o seu nome? '))
print(nome)