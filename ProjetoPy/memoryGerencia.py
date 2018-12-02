#Projeto Sistemas Operacionais 2018.2
#Fabio e Raissa
#Gerenciamento de Memória


#Imports
from random import shuffle

#Define Functions

#---------Open FIle-----------
"""
Abre o Arquivo txt onde estão os processos (Equações)
Retorna uma Lista de Processos aleatórizada
"""
def openfile(path):
    lines = [line.rstrip('\n') for line in open(path)]
    shuffle(lines)
    return lines

#----------------Main-------------
path = "teste.txt"
lista_processo = openfile(path)
for proc in lista_processo:
    print(proc)


