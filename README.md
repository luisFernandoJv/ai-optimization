# 🤖 AI Optimization Algorithms — Portfolio

Implementações do zero de algoritmos clássicos de **Inteligência Artificial e Otimização**, desenvolvidas como parte da disciplina de IA. Todos os algoritmos são escritos em Python puro, sem frameworks de ML.

---

## 📁 Estrutura do Projeto

```
ai-optimization-portfolio/
│
├── hill_climbing/
│   ├── hill_climbing.py           # Subida de encosta com reinício aleatório
│   └── otimizacao_iluminacao.py   # Hill climbing aplicado a cobertura de lâmpadas
│
├── simulated_annealing/
│   └── resfriamento_simulado.py   # Resfriamento simulado (Simulated Annealing)
│
├── genetic_algorithm/
│   └── algoritmo_genetico.py      # AG com elitismo para cobertura de cidades por antenas
│
└── neural_network/
    └── perceptron.py              # Perceptron de Rosenblatt com aprendizado online
```

---

## 🧠 Algoritmos Implementados

### 🏔️ Hill Climbing com Reinício Aleatório

**Arquivo:** `hill_climbing/hill_climbing.py`

Minimiza a soma das distâncias euclidianas de um ponto a 10 centros fixos. Para escapar de ótimos locais, reinicia o processo a partir de posições aleatórias e mantém o melhor resultado encontrado.

**Conceitos:** busca local, ótimo local vs. global, reinício aleatório.

---

### 💡 Otimização de Iluminação

**Arquivo:** `hill_climbing/otimizacao_iluminacao.py`

Minimiza o número de lâmpadas ligadas em um sistema com 100 lâmpadas e 400 casas, garantindo que toda casa seja iluminada por ao menos uma lâmpada. Problema de **cobertura mínima de conjuntos** resolvido via hill climbing.

**Conceitos:** problema de cobertura, restrições de viabilidade, busca local.

---

### 🌡️ Resfriamento Simulado (Simulated Annealing)

**Arquivo:** `simulated_annealing/resfriamento_simulado.py`

Variante do hill climbing que aceita soluções piores com probabilidade `exp(ΔE/T)`, controlada por uma "temperatura" que diminui gradualmente. Inspirado no processo físico de têmpera de metais.

**Conceitos:** critério de Metropolis, schedule de resfriamento, exploração vs. aproveitamento.

| Parâmetro        | Valor  |
| ---------------- | ------ |
| T inicial        | 1000   |
| T mínima         | 0.0001 |
| Resfriamento (α) | 0.999  |

---

### 🧬 Algoritmo Genético — Cobertura por Antenas

**Arquivo:** `genetic_algorithm/algoritmo_genetico.py`

Encontra as melhores posições para 10 antenas em um grid [0,1]² de forma a cobrir o maior número possível de 25 cidades dentro de um raio de 0.1 unidades.

**Mecanismos implementados:**

- Seleção por torneio
- Crossover uniforme
- Mutação por deslocamento
- Elitismo (preservação dos N melhores)

**Conceitos:** população, fitness, seleção, crossover, mutação, elitismo.

---

### 🔬 Perceptron (Rede Neural Simples)

**Arquivo:** `neural_network/perceptron.py`

Implementação do Perceptron de Rosenblatt para classificação binária linear. Aprende a separar pontos pelo sinal da segunda coordenada usando aprendizado online com a regra delta.

**Conceitos:** neurônio artificial, função de ativação degrau, regra de aprendizado do Perceptron, convergência.

---

## ▶️ Como Executar

```bash
# Requer Python 3.10+
# Para visualizações (algoritmo genético):
pip install matplotlib

# Executar qualquer algoritmo:
python hill_climbing/hill_climbing.py
python simulated_annealing/resfriamento_simulado.py
python genetic_algorithm/algoritmo_genetico.py
python neural_network/perceptron.py
```

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualização-orange?style=flat)

- **Linguagem:** Python 3.10+
- **Bibliotecas:** `math`, `random`, `matplotlib` (apenas para gráficos)
- **Paradigma:** Orientado a Objetos + Programação Funcional

---

## 📚 Referências

- Russell, S. & Norvig, P. — _Artificial Intelligence: A Modern Approach_
- Kirkpatrick et al. (1983) — _Optimization by Simulated Annealing_
- Rosenblatt, F. (1958) — _The Perceptron: A Probabilistic Model for Information Storage and Organization_

---

## 👤 Autor

Desenvolvido como parte da disciplina de **Inteligência Artificial**.

> _"Todos os modelos estão errados, mas alguns são úteis."_ — George Box
