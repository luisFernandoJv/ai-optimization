import math
import random

centros = [(-0.0522422357543455, -2.175934043611756), 
           (-9.115993832489925, 9.87023045780461), 
           (-9.482300285090297, 7.078264062229202), 
           (3.1932672836805516, 2.9371082326924114), 
           (2.084449206025198, 4.360955241076596), 
           (8.629139010285193, -5.029177082554773), 
           (3.008865339249496, -5.8560079102363405), 
           (5.265684215948847, -9.57758282402111), 
           (-2.0204975917620427, -2.7703899513300456), 
           (5.290229660165435, 1.0724472556470062)]

def f(pos):
    return 1.0 / sum([math.dist(centro, pos) for centro in centros])

class Estado:
    def __init__(self, pos):
        self.pos = pos
        self.f = f(pos)
    
    def atualiza_f(self, melhor_f, alfa=0.5):
        self.f = alfa * self.f + (1 - alfa) * melhor_f

def mostra_estado(estado):
    print(f'Posição: {estado.pos}, f: {estado.f}')

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
    return melhor(vizinhanca)

def melhor(estados):
    return max(estados, key=lambda e: e.f)

def p(T, deltaE):
    prob = math.exp(deltaE / T)
    return random.uniform(0, 1) < prob

def combina(e, melhor_estado):
    alfa= 0.999
    nova_pos = [0, 0]
    nova_pos[0] = alfa * e.pos[0] + (1 - alfa) * melhor_estado.pos[0]
    nova_pos[1] = alfa * e.pos[1] + (1 - alfa) * melhor_estado.pos[1]
    return Estado(nova_pos)

def atualiza_estados(estados, melhor_estado):
    return [combina(e, melhor_estado) for e in estados]


estados = [estado_inicial() for _ in range(10)]

while True:
    melhor_estado = melhor(estados)
    mostra_estado(melhor_estado)
    estados = atualiza_estados(estados, melhor_estado)