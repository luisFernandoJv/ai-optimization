import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

cidades = [(0.36269182870510597, 0.48774129522533416), (0.4660893990099485, 0.625977277322444), (0.8745272049602363, 0.8430847178413662), (0.9056648689941714, 0.12534220902163062), (0.9421756770754608, 0.43767834728011523), (0.3454151547493155, 0.758167186040258), (0.813468568474946, 0.8552989784378868), (0.4851334713924228, 0.4127340682039369), (0.029680439099751377, 0.6411731474557683), (0.0702889108622674, 0.14791539299640677), (0.24556253406244766, 0.10571560952377279), (0.2954378132119899, 0.08644637363420238), (0.12193997105850451, 0.835169099471723), (0.5672551319530861, 0.9724779953778995), (0.14299661850631318, 0.3120363673605189), (0.27583525745726467, 0.8300733816371841), (0.15715159004116763, 0.5955251687327586), (0.27303620360181813, 0.9990729491762935), (0.5221922976395411, 0.6761151065261006), (0.40433179879713665, 0.23361500394452572), (0.3064391015189115, 0.02513740951343202), (0.486198461173006, 0.8415592046693033), (0.041597840573812106, 0.5670269392321446), (0.794198584338026, 0.4080839888992256), (0.8425372847437997, 0.10388675264261027)]

def f(antenas):
    contador = 0
    for cidade in cidades:
        for antena in antenas:
            if math.dist(antena, cidade) < 0.1:
                contador += 1
                break
    return contador 

class Estado:
    def __init__(self, antenas):
        self.antenas = antenas
        self.f = f(antenas)

# Função de escolha usando seleção por torneio
def escolhe(populacao):
    candidato1 = random.choice(populacao)
    candidato2 = random.choice(populacao)
    return candidato1 if candidato1.f > candidato2.f else candidato2

# Função de cruzamento
def cruzamento(pai1, pai2):
    antenas = []
    
    for i in range(len(pai1.antenas)):
        antena = pai1.antenas[i]
        if(random.uniform(0, 1) < 0.5):
          antena = pai2.antenas[i]
          
        antenas.append(antena) 
         
    return Estado(antenas)

# Função de mutação que altera aleatoriamente uma antena

def mutacao(estado):
   deltaX = random.uniform(-0.1, 0.1)
   deltaY = random.uniform(-0.1, 0.1)
   i = random.randint(0, len(estado.antenas) - 1)
   antenas = estado.antenas
   estado.antenas[i] = (estado.antenas[i][0] + deltaX,estado.antenas[i][1] + deltaY )
   
   return Estado(estado.antenas)
   
   
# Configurações do algoritmo genético
N = 50  # Tamanho da população
n_geracoes = 100  # Número de gerações
taxa_mutacao = 0.1  # Taxa de mutação

# Inicializa a população
populacao = [Estado([(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(10)]) for _ in range(N)]

# Evolução da população
n_elite = 5

for _ in range(n_geracoes):
    prox = []
    for _ in range(N - n_elite):
        pai1 = escolhe(populacao)
        pai2 = escolhe(populacao)
        filho = cruzamento(pai1, pai2)
        if random.uniform(0, 1) < taxa_mutacao:
            filho = mutacao(filho)
        prox.append(filho)
        
    populacao = sorted(populacao,key=lambda estado: estado.f, reverse = True )
    populacao = populacao[:n_elite] + prox

# Escolhe o melhor estado
estado = max(populacao, key=lambda estado: estado.f)
print(f'Melhor solução cobre {estado.f} cidades')

# Gráfico das cidades e antenas
x = [cidade[0] for cidade in cidades]
y = [cidade[1] for cidade in cidades]

fig = plt.figure()
ax = fig.add_subplot()

# Plotando as cidades
ax.scatter(x, y, color='black')

# Plotando as antenas com elipses
for antena in estado.antenas:
    e = Ellipse(antena, width=0.2, height=0.2, angle=0)
    e.set_alpha(0.6)
    ax.add_artist(e)

plt.show()
