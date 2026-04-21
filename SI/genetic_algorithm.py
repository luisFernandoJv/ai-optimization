"""
Algoritmo Genético — Cobertura de Cidades por Antenas
Encontra posições para N antenas que maximizem o número de cidades cobertas
dentro de um raio de 0.1 unidades.
"""

import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


CIDADES = [
    (0.363, 0.488), (0.466, 0.626), (0.875, 0.843), (0.906, 0.125),
    (0.942, 0.438), (0.345, 0.758), (0.813, 0.855), (0.485, 0.413),
    (0.030, 0.641), (0.070, 0.148), (0.246, 0.106), (0.295, 0.086),
    (0.122, 0.835), (0.567, 0.972), (0.143, 0.312), (0.276, 0.830),
    (0.157, 0.596), (0.273, 0.999), (0.522, 0.676), (0.404, 0.234),
    (0.306, 0.025), (0.486, 0.842), (0.042, 0.567), (0.794, 0.408),
    (0.843, 0.104),
]

RAIO_COBERTURA = 0.1
N_ANTENAS      = 10

# Hiperparâmetros do AG
TAMANHO_POPULACAO = 50
N_GERACOES        = 200
TAXA_MUTACAO      = 0.15
N_ELITE           = 5
DELTA_MUTACAO     = 0.1


def cobertura(antenas: list[tuple]) -> int:
    """Conta quantas cidades são cobertas por pelo menos uma antena."""
    return sum(
        any(math.dist(antena, cidade) < RAIO_COBERTURA for antena in antenas)
        for cidade in CIDADES
    )


class Individuo:
    def __init__(self, antenas: list[tuple]):
        self.antenas = list(antenas)
        self.f = cobertura(antenas)

    def __repr__(self):
        return f"Individuo(cobertura={self.f}/{len(CIDADES)})"


def individuo_aleatorio() -> Individuo:
    antenas = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(N_ANTENAS)]
    return Individuo(antenas)


def selecao_torneio(populacao: list[Individuo]) -> Individuo:
    """Seleciona o melhor entre dois candidatos aleatórios."""
    c1, c2 = random.sample(populacao, 2)
    return c1 if c1.f >= c2.f else c2


def cruzamento(pai1: Individuo, pai2: Individuo) -> Individuo:
    """Crossover uniforme: cada antena vem de um dos pais com prob. 0.5."""
    antenas = [
        pai1.antenas[i] if random.random() < 0.5 else pai2.antenas[i]
        for i in range(N_ANTENAS)
    ]
    return Individuo(antenas)


def mutacao(individuo: Individuo) -> Individuo:
    """Desloca aleatoriamente uma antena sorteada."""
    antenas = individuo.antenas.copy()
    i = random.randint(0, N_ANTENAS - 1)
    x, y = antenas[i]
    antenas[i] = (
        max(0, min(1, x + random.uniform(-DELTA_MUTACAO, DELTA_MUTACAO))),
        max(0, min(1, y + random.uniform(-DELTA_MUTACAO, DELTA_MUTACAO))),
    )
    return Individuo(antenas)


def algoritmo_genetico() -> Individuo:
    populacao = [individuo_aleatorio() for _ in range(TAMANHO_POPULACAO)]

    for geracao in range(N_GERACOES):
        # Elitismo: preserva os melhores
        elite = sorted(populacao, key=lambda ind: ind.f, reverse=True)[:N_ELITE]

        # Gera nova geração por cruzamento + mutação
        nova_geracao = []
        while len(nova_geracao) < TAMANHO_POPULACAO - N_ELITE:
            pai1 = selecao_torneio(populacao)
            pai2 = selecao_torneio(populacao)
            filho = cruzamento(pai1, pai2)
            if random.random() < TAXA_MUTACAO:
                filho = mutacao(filho)
            nova_geracao.append(filho)

        populacao = elite + nova_geracao

        if (geracao + 1) % 50 == 0:
            melhor = max(populacao, key=lambda ind: ind.f)
            print(f"Geração {geracao+1:>3}: {melhor}")

    return max(populacao, key=lambda ind: ind.f)


def plotar_resultado(melhor: Individuo):
    xs = [c[0] for c in CIDADES]
    ys = [c[1] for c in CIDADES]

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title(f"Cobertura: {melhor.f}/{len(CIDADES)} cidades", fontsize=14)
    ax.scatter(xs, ys, color="black", zorder=5, label="Cidades")

    for i, antena in enumerate(melhor.antenas):
        e = Ellipse(antena, width=2 * RAIO_COBERTURA, height=2 * RAIO_COBERTURA,
                    alpha=0.35, color="steelblue")
        ax.add_patch(e)
        ax.plot(*antena, "r^", markersize=6)

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.legend()
    plt.tight_layout()
    plt.savefig("cobertura_antenas.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    random.seed(42)
    melhor = algoritmo_genetico()
    print(f"\nMelhor solução: {melhor}")
    plotar_resultado(melhor)