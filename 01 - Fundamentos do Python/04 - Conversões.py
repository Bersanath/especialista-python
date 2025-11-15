'''
A conversão em python nos permite converter um tipo primitivo para um outro tipo como por exemplo de inteiro para real de real para inteiro
'''

real = int(1.24535) # Aqui nós estamos a fazer a conversão de um número real para um número inteiro, vamos sair de um tipo para outro ela vai descartar toda a parte decimal e vai ficar apenas com a parte inteira
print(type(real))

inteiro = float(10) # Aqui estamos a fazer o inverso estamos a sair de um número inteiro para um número real
print(inteiro)

# Esse tipo de conversão também pode funcionarar com um texto, mais com pórem ele só funciona se o texto for '2342' ou "424" mais se for "Eduado" ele não vai funcionar, e tivermos uma string com números reais temos que converter para números reais não inteiro por que também não vai funcionar

texto = int('123')
print(texto)

numero = str(2001)
print(type(numero))

print(bool(20))