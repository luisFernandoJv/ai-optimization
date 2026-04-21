import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

#algoritmo_generico
centros = [(-0.0522422357543455, -2.175934043611756), (-9.115993832489925, 9.87023045780461), (-9.482300285090297, 7.078264062229202), (3.1932672836805516, 2.9371082326924114), (2.084449206025198, 4.360955241076596), (8.629139010285193, -5.029177082554773), (3.008865339249496, -5.8560079102363405), (5.265684215948847, -9.57758282402111), (-2.0204975917620427, -2.7703899513300456), (5.290229660165435, 1.0724472556470062)]

def f(pos):
    return 1.0/sum([math.dist(centro, pos) for centro in centros])

class Estado:                                                                 
    def __init__(self, pos):
        self.pos = pos
        self.f = f(pos)

def mostra_estado(estado):
    print(f'Posição: {estado.pos}, f: {1.0/estado.f}')

def estado_inicial():
    return Estado([random.uniform(-10, 10), random.uniform(-10, 10)])

def muda(estado):
    deltaX = random.uniform(-1, 1)
    deltaY = random.uniform(-1, 1)
    return Estado([estado.pos[0] + deltaX, estado.pos[1] + deltaY])

def vizinhos(estado):
    return [muda(estado) for _ in range(10)]

def melhor_sucessor(estado):
    vizinhanca = vizinhos(estado)
    return max(vizinhanca, key=lambda e: e.f)

def p(T, deltaE):
    prob = math.exp(deltaE/T)
    return random.uniform(0, 1) < prob

T = 1000
#população = populaão_inicial()
atual = estado_inicial()

#enquanto(criterio = tantas gerações):

while (T > 0.0001):
    T = 0.999*T
    #para i in 1 até N:
    vizinho = melhor_sucessor(atual)
    deltaE = vizinho.f - atual.f
    if (deltaE > 0 or p(T, deltaE)):
        atual = vizinho
        mostra_estado(atual)
        

#pai1 = seleciona(população)
#pai2 = seleciona(população)
#filho = cruzamento(pai1, pai2)
# se (prob()<taxa_de_mutação):
    #filho = mutação(filho)
    
#prox_geração.append(filho)
#população = prox_geração.append(filho)