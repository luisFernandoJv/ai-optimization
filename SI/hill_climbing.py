import math
import random

centros = [(-0.0522422357543455, -2.175934043611756), (-9.115993832489925, 9.87023045780461), (-9.482300285090297, 7.078264062229202), (3.1932672836805516, 2.9371082326924114), (2.084449206025198, 4.360955241076596), (8.629139010285193, -5.029177082554773), (3.008865339249496, -5.8560079102363405), (5.265684215948847, -9.57758282402111), (-2.0204975917620427, -2.7703899513300456), (5.290229660165435, 1.0724472556470062)]

def f(pos):
    return sum([math.dist(centro, pos) for centro in centros])

class Estado:
    def __init__(self, pos):
        self.pos = pos
        self.f = f(pos)

def mostra_estado(estado):
    print(f'PosiÃ§Ã£o: {estado.pos}, f: {estado.f}')

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
    return min(vizinhanca, key=lambda e: e.f)

melhor_f = 100
while True:

   atual = estado_inicial()
   while True:
       vizinho = melhor_sucessor(atual)

       if vizinho.f >= atual.f:
           break

       atual = vizinho

   if(atual.f < melhor_f):
   	mostra_estado(atual)
   	melhor_f = atual.f