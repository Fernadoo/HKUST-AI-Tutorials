# -*- coding: utf-8 -*-
# You need to first install numpy, matplotlib, seaborn

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


class indivdual:
    def __init__(self):
        self.x = 0  # genome
        self.fitness = 0  # fitness value

    def __eq__(self, other):
        self.x = other.x
        self.fitness = other.fitness


def fitness(x):
    return x * np.sin(10 * np.pi * x) + 2


def initPopulation(pop, N):
    for i in range(N):
        ind = indivdual()
        ind.x = np.random.uniform(-1, 2)
        ind.fitness = fitness(ind.x)
        pop.append(ind)


def selection(N):
    # randomly select two parents for crossover
    return np.random.choice(N, 2)


def crossover(parent1, parent2):
    child1, child2 = indivdual(), indivdual()
    child1.x = 0.9 * parent1.x + 0.1 * parent2.x
    child2.x = 0.1 * parent1.x + 0.9 * parent2.x
    child1.fitness = fitness(child1.x)
    child2.fitness = fitness(child2.x)
    return child1, child2


def mutation(pop):
    ind = np.random.choice(pop)
    ind.x = np.random.uniform(-1, 2)
    ind.fitness = fitness(ind.x)


def evolve():
    ###################################################
    # You may change these numbers to see what happens#
    ###################################################
    N = 100  # size of the population
    POP = []  # the population
    iter_N = 100  # number of iterations
    mut_prob = 0.1  # matate with prob mut_prob

    initPopulation(POP, N)

    for it in range(iter_N):
        a, b = selection(N)
        if np.random.random() < 0.75:  # crossover w.p. 0.75
            child1, child2 = crossover(POP[a], POP[b])
            new = sorted([POP[a], POP[b], child1, child2],
                         key=lambda ind: ind.fitness,
                         reverse=True)
            POP[a], POP[b] = new[0], new[1]

        if np.random.random() < mut_prob:
            mutation(POP)

        POP.sort(key=lambda ind: ind.fitness, reverse=True)

    return POP


# Visualization

scatter_x = []
for count in range(10):
    pop = evolve()
    print(pop[0].x, fitness(pop[0].x))  # the best in this population
    scatter_x.append(pop[0].x)
scatter_y = np.array([fitness(x) for x in scatter_x])

x = np.linspace(-1, 2, 100000)
y = fitness(x)
plt.plot(x, y)
plt.scatter(scatter_x, scatter_y, c='r')
plt.show()
# plt.savefig("./func.png",dpi=500)
