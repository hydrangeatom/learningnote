'''
    nurse scheduling problem (shift scheduling)
    optimize the shift scheduling with genetic algorithm
'''

from random import randint, random, shuffle
import numpy as np

class SimpleGA:
    def __init__(self, n_pop, n_gen, ratio_select, prob_mut):
        self.n_pop = n_pop
        self.n_gen = n_gen
        self.ratio_select = ratio_select
        self.prob_mut = prob_mut
        self.optimals = []

    def __init_pop(self):
        new_pop = []
        for _ in range(self.n_pop):
            indv = self.create_indv()
            new_pop.append(indv)
        self.pop = new_pop
    
    def __exclude_lethal(self):
        new_pop = []
        for indv in self.pop:
            if not self.is_lethal(indv):
                new_pop.append(indv)
        self.pop = new_pop

    def __calc_fitness(self):
        fitness_raw = []
        for indv in self.pop:
            f_indv = self.calc_fitness(indv)
            fitness_raw.append(f_indv)
        fitness_raw = np.array(fitness_raw)

        # normalize fitness
        fitness = np.array(fitness_raw)
        f_min, f_max = np.min(fitness), np.max(fitness)
        if np.allclose(f_min, f_max): 
            fitness = np.ones(*fitness.shape)
        else:
            fitness = (fitness - f_min) / (f_max - f_min)
        fitness = fitness / np.sum(fitness)

        for indv, f_raw, f in zip(self.pop, fitness_raw, fitness):
            indv.fitness_raw = f_raw
            indv.fitness = f

    def __selection(self):
        # ranking selection
        selected = sorted(self.pop, key=lambda indv: indv.fitness, reverse=True)
        selected = selected[:int(self.n_pop*self.ratio_select)]
        new_pop = []
        while len(new_pop) < self.n_pop:
            new_pop += list(selected)
        new_pop = new_pop[:self.n_pop]
        self.pop = new_pop
        self.optimals.append(selected[0])

    def __crossover(self):
        shuffle(self.pop)
        new_pop = []
        for parent1, parent2 in zip(self.pop, self.pop[:-1]+[self.pop[0]]):
            child = self.crossover(parent1, parent2)
            new_pop.append(child)
        self.pop = new_pop

    def __mutation(self):
        for i in range(self.n_pop):
            if random() < self.prob_mut:
                self.pop[i] = self.mutate(self.pop[i])
           
    def __print_by_gen(self, i_gen):
        f = list(map(lambda i: i.fitness_raw, self.pop))
        f_max, f_avg, f_min = max(f), sum(f)/len(f), min(f)
        print(f'gen={i_gen} fitness max={f_max:.2f} avg={f_avg:.2f} min={f_min:.2f}')

    def run(self):
        self.__init_pop()
        for i in range(self.n_gen):
            self.__exclude_lethal()
            self.__calc_fitness()
            self.__selection()
            self.__print_by_gen(i)
            if i == self.n_gen-1: break
            self.__crossover()
            self.__mutation()
 
    def get_optimal(self):
        indv_max = None
        for indv in self.pop:
            if not indv_max or indv_max.fitness_raw < indv.fitness_raw:
                indv_max = indv
        return indv_max

class Roster:
    def __init__(self, roster):
        self.roster = roster
        self.fitness_raw = -1
        self.fitness = -1

    def __getitem__(self, i):
        return self.roster[i]

    def __len__(self):
        return len(self.roster)
    
    def __repr__(self):
        return f'fitness={self.fitness_raw} roster={self.roster}'

class RosterConditions:
    def __init__(self):
        self.n_days = 100
        self.n_members = 8

        self.weights = []
        for i in range(self.n_days):
            if   0 <= i % 7 <= 3 : w = 1.  # Mon-Thu
            elif i % 7 == 4      : w = 2.  # Fri
            elif i % 7 == 5      : w = 3.  # Sat
            else                 : w = 4.  # Sun
            if i <= 30 : w *= 1.5  # the first month
            self.weights.append(w)

    def create_roster(self):
        offset = randint(0, self.n_members-1)
        roster = []
        for i in range(self.n_days):
            member = (offset+i) % self.n_members
            roster.append(member)
        return Roster(roster)

    # hard constraint
    def is_lethal(self, roster):
        # one or zero shift in three days
        for i in range(self.n_days-3):
            if len(set(roster[i:i+3])) < 3:
                return True
        # no concecutive sunday shift
        for m1, m2 in zip(roster[6::7], roster[13::7]):
            if m1==m2:
                return True
        return False

    # soft constraint
    def calc_fitness(self, roster):
        # the equiality of the weight
        total_weight = [0] * self.n_members
        for member, weight in zip(roster, self.weights):
            total_weight[member] += weight
        weight_min_max = max(total_weight) - min(total_weight)
        return -weight_min_max

    def crossover(self, roster1, roster2):
        p = randint(0, len(roster1))
        new_roster = Roster(roster1[:p] + roster2[p:])
        return new_roster

    def mutate(self, roster):
        p1 = randint(0, len(roster)-1)
        p2 = randint(0, len(roster)-1)
        chunk1 = roster[p1:p2]
        chunk2 = roster[:p1] + roster[p2:]
        p3 = randint(0, len(chunk2)-1)
        new_roster = Roster(chunk2[:p3] + chunk1 + chunk2[p3:])
        return new_roster

def main():
    ga = SimpleGA(n_pop=50, n_gen=100, ratio_select=0.4, prob_mut=0.3)
    rc = RosterConditions()
    ga.create_indv = rc.create_roster
    ga.is_lethal = rc.is_lethal
    ga.calc_fitness = rc.calc_fitness
    ga.crossover = rc.crossover
    ga.mutate = rc.mutate
    ga.run()
    print('optimal is ... ', ga.get_optimal())

if __name__=='__main__':
    main()
