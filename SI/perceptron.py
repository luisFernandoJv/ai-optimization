"""
Perceptron — Aprendizado Online
Aprende a classificar pontos (x0, x1) como positivos (x1 > 0) ou negativos
usando a regra de aprendizado do Perceptron de Rosenblatt.
"""

import random


# Taxa de aprendizado
TAXA = 0.01
MAX_ITERACOES = 10_000


def ativacao(entrada: float) -> int:
    """Função de ativação degrau: +1 se entrada > 0, senão -1."""
    return 1 if entrada > 0 else -1


def treinar_perceptron(taxa: float = TAXA, max_iter: int = MAX_ITERACOES):
    """
    Treina um Perceptron de 2 entradas para classificar pontos pelo sinal de x1.
    Retorna os pesos finais e o número de erros acumulados.
    """
    pesos = [0.0, -1.0]  # w0, w1
    erros_total = 0

    for iteracao in range(max_iter):
        # Gera amostra aleatória
        x = [random.uniform(-1, 1), random.uniform(-1, 1)]
        esperado = 1 if x[1] > 0 else -1

        # Forward pass
        entrada_ponderada = sum(pesos[i] * x[i] for i in range(len(pesos)))
        saida = ativacao(entrada_ponderada)

        # Atualização dos pesos (regra do Perceptron)
        erro = esperado - saida
        if erro != 0:
            erros_total += 1
            for i in range(len(pesos)):
                pesos[i] += taxa * x[i] * erro

        # Avaliação periódica
        if (iteracao + 1) % 1000 == 0:
            acuracia = avaliar_perceptron(pesos, n_amostras=500)
            print(f"  Iter {iteracao+1:>6} | Pesos: [{pesos[0]:+.4f}, {pesos[1]:+.4f}] "
                  f"| Acurácia: {acuracia:.1%}")

    return pesos, erros_total


def avaliar_perceptron(pesos: list[float], n_amostras: int = 1000) -> float:
    """Retorna a acurácia do perceptron em amostras aleatórias."""
    acertos = 0
    for _ in range(n_amostras):
        x = [random.uniform(-1, 1), random.uniform(-1, 1)]
        esperado = 1 if x[1] > 0 else -1
        entrada = sum(pesos[i] * x[i] for i in range(len(pesos)))
        if ativacao(entrada) == esperado:
            acertos += 1
    return acertos / n_amostras


if __name__ == "__main__":
    random.seed(42)
    print("Treinando Perceptron...")
    print(f"  Taxa de aprendizado : {TAXA}")
    print(f"  Máx. de iterações   : {MAX_ITERACOES}\n")

    pesos_finais, total_erros = treinar_perceptron()
    acuracia_final = avaliar_perceptron(pesos_finais)

    print(f"\nResultado final:")
    print(f"  Pesos aprendidos : w0={pesos_finais[0]:+.4f}, w1={pesos_finais[1]:+.4f}")
    print(f"  Total de erros   : {total_erros}")
    print(f"  Acurácia final   : {acuracia_final:.1%}")