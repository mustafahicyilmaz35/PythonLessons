# -*- coding: utf-8 -*-
import random


class Supurge_dunyasi():
    def __init__(self):
        self.durumlar = {'lok_A': random.choice(['Temiz', 'Kirli']),
                         'lok_B': random.choice(['Temiz', 'Kirli'])}
        self.done = False

    def hareket_al(self, agent, hareket):
        if (hareket == 'Sağ'):
            agent.locatation = 'lok_B'
            agent.performance -= 1
        elif (hareket == 'Sol'):
            agent.locatation = 'lok_A'
            agent.performance -= 1
        elif (hareket == 'Çek'):
            if (self.durumlar[agent.locatation] == "Kirli"):
                agent.performance += 10
                self.durumlar[agent.locatation] = "Temiz"
        if self.durumlar["lok_A"] == "Temiz" and self.durumlar["lok_B"] == "Temiz":
            self.done = True

    def random_baslangic(self):
        return random.choice(["lok_A", "lok_B"])


class Agent():
    def __init__(self, location):
        self.performance = 0
        self.location = location

    def hareket_sec(self):
        return random.choice(["Sağ", "Sol", "Çek"])


env = Supurge_dunyasi()
agent = Agent(env.random_baslangic)
while (not env.done):
    agent_hareketi = agent.hareket_sec()
    print(agent_hareketi)
    print(agent.location)
    print(env.durumlar)
    env.hareket_al(agent, agent_hareketi)
print(agent.performance)
