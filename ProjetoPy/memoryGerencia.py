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

memory = []
index = []
size = 0
def openfile(path):
    lines = [line.rstrip('\n') for line in open(path)]
    return lines
def calculateCost(proc):
    #print(proc)
    result = ''.join([i for i in proc if not i.isdigit()])
    #print(result)
    cost = 0
    for i in result:
        if i == '+' or i =='-':
            cost += 1
        elif i == '*' or i =='/':
            cost += 3
        elif i == '^':
            cost += 5
    return cost
def inicialize_memory():
    for n in range(50):
        print(n)
        memory.append(0)
        index.append(0)

def incert_into_memory(id, cost):
    index_start = 0
    index_fim = 0
    pointer = 0
    count = 0
    for slot in index:
        if slot == 0:
            count += 1
        else:
            count = 0
            index_start = pointer +1
        if count == cost:
            index_fim = pointer
        pointer += 1
    


#----------------Main-------------
path = "equations.txt"
inicialize_memory()
lista_processo = openfile(path)
id = 0
"""
for proc in lista_processo:
    #print(proc)
    size = calculateCost(proc)
    incert_into_memory(id, cost)
    id += 1
"""
incert_into_memory(0,5)

