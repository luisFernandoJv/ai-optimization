import random 
import math

centros = [(-0.02317894799976794, -0.6664547106683611)]
[(0.9994648183691854, 0.7482660944719024)]
[(0.8812383876623255, 0.7682982752964107)]
[(0.7673147645296232, 0.43450084620714624)]
[(-0.6054367447547073, 0.6349919064749043)]
[(-0.6456019421083354, -0.12335038652091401)]
[(-0.5898884427079807, 0.6231529679923988)]
[(0.3859904759550885, 0.11017058731403617)]
[(-0.22253126191862793, 0.9059926212590228)]
[(0.997722728204119, -0.7092086295216451)]

def objetivo(usinas):
    cont = 0
    lusinas = usinas 
    for centro in centros:
        for lusina in lusinas:
            (xc, yc) = centro
            (xu, yu) = lusina
            distancia = math.sqrt((xc-xu)**2+(yc - yu)**2)
            cont = cont + distancia
    return cont

class Estado:
    
    usinas = (0, 0)
    
    f = 0
    
    def __init__(self, usinas_):
       self.usinas = usinas_.copy()
       self.f = objetivo(self.usinas)
       
       
    def exibe(self):
        print(f"Usinas:{self.usinas}, {self.f}")
    
    def mutacao(self):
        usinas = self.usinas.copy()
        deltaX = random.uniform(-1, 1)
        deltaY = random.uniform(-1, 1)
        (x, y) = usinas[0]
        usinas = [(x + deltaX, y + deltaY)]
        return Estado(usinas)

def cruzamento(self, pai):
    usinas = self.usinas.copy()
    moeda = random.uniform(0, 1)
    if moeda < 0.5:
        (x, y) = pai.usinas[0]
        usinas = [(x, y)]
    return Estado(usinas)

#variavies de tamanho da minha população
t_p = 50
n_alteracoes = 10
taxa_m = 0.1

def escolhe(populacao):
    n = len(populacao)
    i1 = random.uniform(0, n-1)
    i2 = random.uniform(0, n-1)
    if (populacao[i1].f < populacao[i2].f):
        return populacao
    
    return populacao[i2]

populacao = []
print('Primeira geração: ')
for i in range(t_p):
    usinas = (0, 0)
    individuo = Estado(usinas)
    populacao.append(individuo)
    individuo.exibe()

n_geracoes = 20
for i in range(n_geracoes):
    prox = []
    
    for j in range(n_geracoes):
        in1 = escolhe(populacao)
        in2 = escolhe(populacao)
        filho = in1>cruzamento(in2)
        if(random.uniforme(0, 1)< 0.5):
            filho = filho.mutacao()
        prox.append(filho)
        populacao = prox
        
        
        
    print('Geração')
    filho.exibe()
    
    print("Ultima geração: ")
