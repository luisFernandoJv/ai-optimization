"""
Resfriamento Simulado (Simulated Annealing)
Maximiza 1/soma_distâncias — equivalente a minimizar a soma de distâncias
a um conjunto de centros, permitindo aceitar soluções piores com probabilidade
controlada pela temperatura T.
"""

import math
import random


CENTROS = [
    (-0.052, -2.175), (-9.115, 9.870), (-9.482, 7.078),
    (3.193, 2.937),   (2.084, 4.360),  (8.629, -5.029),
    (3.008, -5.856),  (5.265, -9.577), (-2.020, -2.770),
    (5.290, 1.072),
]

# Hiperparâmetros
T_INICIAL    = 1_000.0
T_MINIMA     = 0.0001
RESFRIAMENTO = 0.999
N_VIZINHOS   = 10


def funcao_objetivo(pos: list[float]) -> float:
    """Retorna 1/soma_distâncias (quanto maior, melhor)."""
    soma = sum(math.dist(c, pos) for c in CENTROS)
    return 1.0 / soma


class Estado:
    def __init__(self, pos: list[float]):
        self.pos = pos
        self.f = funcao_objetivo(pos)

    def soma_distancias(self) -> float:
        return 1.0 / self.f

    def __repr__(self):
        return f"Estado(pos={[round(v,4) for v in self.pos]}, soma_dist={self.soma_distancias():.4f})"


def estado_inicial() -> Estado:
    return Estado([random.uniform(-10, 10), random.uniform(-10, 10)])


def gerar_vizinho(estado: Estado) -> Estado:
    return Estado([
        estado.pos[0] + random.uniform(-1, 1),
        estado.pos[1] + random.uniform(-1, 1),
    ])


def melhor_vizinho(estado: Estado) -> Estado:
    vizinhos = [gerar_vizinho(estado) for _ in range(N_VIZINHOS)]
    return max(vizinhos, key=lambda e: e.f)


def aceita_pior(T: float, delta_e: float) -> bool:
    """Aceita solução pior com probabilidade exp(ΔE/T)."""
    return random.random() < math.exp(delta_e / T)


def resfriamento_simulado() -> Estado:
    T = T_INICIAL
    atual = estado_inicial()
    melhor = atual

    while T > T_MINIMA:
        T *= RESFRIAMENTO
        vizinho = melhor_vizinho(atual)
        delta_e = vizinho.f - atual.f

        if delta_e > 0 or aceita_pior(T, delta_e):
            atual = vizinho
            if atual.f > melhor.f:
                melhor = atual

    return melhor


if __name__ == "__main__":
    random.seed(42)
    resultado = resfriamento_simulado()
    print("Melhor solução encontrada:")
    print(f"  Posição        : {resultado.pos}")
    print(f"  Soma distâncias: {resultado.soma_distancias():.6f}")