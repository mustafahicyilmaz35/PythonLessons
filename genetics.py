"""
Spyder Editor

This is a temporary script file.
"""
""" hareket kapasitesi kadar durumumuz var, dört hareketimiz var
bunlar, aşağı, yukarı, sol ve sağdır."""

"""birey =[1,2,3,4,1,2,3,4...] = 16 gen"""
"""pop sayısı kadar birey
10x birey"""

"""Birinci jenerasyon"""


"""10x birey [1,2,3,4,1,2,3,4...]
fitnes function oyundan aldığım ödül, bu fonk a göre 2 elite seçilecek,
8 tane kalacak, 8 kişi 2 li 2 li üretilecek
b1[1,2,3,4,1,2,3,4..] b2[1,2,3,4,1,2,3,4...]
a1[1,2,3,4,1,2,3,4] a2[1,2,3,4...,1,2,3,4]
bu sırada mutasyonlar olabilir. Bu işlem sonucunda yene jenerasyonlar oluşacak ve
son jenerasyon en iyisi olacak."""

import numpy as np
import gym
import matplotlib.pyplot as plt

""" Burada make fonksiyonu ile ortamı oluşturuyoruz. v0 ise 4x4 kombinasyonunu
oluşturacak."""
env = gym.make("FrozenLake-v0")

""" Kaç bireyle oyun oynayacağımızı belirler """
population_size = 50
""" Kaç tane durumum olduğunu söyleyecek."""
gene_size = env.observation_space.n
""" 4 tane gen(hareket) opsiyonum var. Sağ, Sol, Yukarı, Aşağı """
gene_options = 4

""" 20 jenerasyonda bulmasını istediğim için 20 değerini kullandım """
generation_number = 20
""" Kaç tane elit seçeceğim. Her jenerasyonda 4 tane yeterli """
elite_pop_size = 4
""" 100 tekrardan sonra bitir. """
n_episode = 100
""" Mutasyon İhtimali """
mutataion_chance = 0.05

def cross_over_with_pieces_of_parent(parent1,parent2):
    pos = np.random.randint(gene_size)
    """ Dizilerin ilk yarısını[:pos] ve ikinci yarısını aldık.[pos:] """
    child1 = np.concatenate((parent1[:pos],parent2[pos:]),axis = 0)
    child2 = np.concatenate((parent1[pos:],parent2[:pos]),axis = 0)
    for i in np.arange(gene_size):
        if(np.random.uniform() < mutataion_chance):
            child1[i] = np.random.randint(4)
    for i in np.arange(gene_size):
        if(np.random.uniform() < mutataion_chance):
            child2[i] = np.random.randint(4)
    return child1, child2
def cross_over_with_digit(parent1,parent2):
    children = {0:np.random.randint(gene_options,size = gene_size),
                1:np.random.randint(gene_options,size = gene_size) }
    for child in range(2):
        for gene in range(gene_size):
            if(np.random.uniform() < mutataion_chance):
                children[child][gene] = np.random.randint(4)
            else:
                if np.random.uniform()<0.5:
                    children[child][gene] = parent1[gene]
                else:
                    children[child][gene] = parent2[gene]
    return children[0],children[1]


def play_agent(agent,episode,env):
    total_reward = 0
    for ep in range(episode):
        """ Başlangıç durumunu döner """
        state = env.reset()
        while(True):
            action = agent[state]
            """Yeni durum, ödül, oyunu kazandım mı?"""
            next_state, reward, done, info = env.step(action)
            if done:
                total_reward += reward
                break
            state = next_state
    return total_reward/episode
    
population = [np.random.randint(gene_options,size=gene_size) for _ in range(population_size)]
best_scores_with_peaces_crossover = []

for n in range(generation_number):
        fitness_scores = []
        for invidiual in population:
            fitness_scores.append(play_agent(invidiual,n_episode,env))
        best_invidiual = np.max(fitness_scores)
        best_scores_with_peaces_crossover.append(best_invidiual)
        population_ranks = list(reversed(np.argsort(fitness_scores)))
        elite_pop = [population[x] for x in population_ranks[:elite_pop_size]]
        select_probs = np.array(fitness_scores)/np.sum(fitness_scores)
        child_set = []
        for generate in range(23):
            children = cross_over_with_pieces_of_parent(population[np.random.choice(range(population_size), p=select_probs)],
                                                                   population[np.random.choice(range(population_size), p=select_probs)])
            child_set.append(children[0])
            child_set.append(children[1])
        population = child_set + elite_pop
y1 = best_scores_with_peaces_crossover
x = np.arange(20)
plt.plot(x,y1)
plt.title("Genetik Sonuçlar")
plt.show()
