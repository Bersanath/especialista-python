'''
    Set é um conjunto de dados que armazena apenas uma valor único e não contém valores repetidos, se por acso tiver números repetidos ele ignora um valor e matem o outro
'''

conjunto = set()
conjunto2 = {2,'as',(1,2,3,4), True,'as',2}
conjunto2.add('Eduardo') # O método add() nos permitem adicionar elemento no nosso set()
conjunto2.update(['Pedro','Jorge','Tecacunda']) # O método update() nos permiti adicionar varios elementos
conjunto2.discard(True) # O método discard() nos permiti descartar um elemento que se encontra no nosso set()
print(conjunto2)
