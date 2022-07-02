import copy
import heapq
import random

from tools.fitness import fitness, generate_route
from tools.cross_over import cross_over


class GeneticAlgorithm:
    '''
    Clase que modela el problema. 
    Recibe los clientes, sus identificadores, la capacidad del vehículo y la cantidad de vehículos.
    Cada ruta es un cromosoma y son modelados como listas. 
    Cada individuo corresponde al total de clientes en una ruta, los cuales son guardados en una lista simple.
    '''

    def __init__(self, clients, clients_id, capacity_vehicle, count_vehicle):
        self.clients = clients
        self.clients_id = clients_id
        self.capacity_vehicle = capacity_vehicle
        self.count_vehicle = count_vehicle

    def mutation(self, clients_id):
        start, stop = sorted(random.sample(range(len(clients_id)), 2))
        cromo = clients_id[:start] + \
            clients_id[stop:start-1:-1] + clients_id[stop+1:]
        return cromo


def genetic_algorithm(metaheuristic, k, ngen, size, ratio_cross, prob_mutate, distances):
    '''
    k participantes en el torneo, size=tamaño de poblacion
    '''

    def initial_population(metaheuristic, size):
        '''
        se crean los cromosomas aleatoriamente, luego se crea una poblacion inicial 
        de cromosomas de acuerdo al tamaño elegido (size)
        '''
        population = []
        individue = metaheuristic.clients_id
        for _ in range(size):
            random.shuffle(individue)
            aux = copy.deepcopy(individue)
            population.append(aux)
        return population

    def new_generation(metaheuristic, k, population, n_parents, n_directs, prob_mutate):

        def selection(metaheuristic, population, n):
            heapq.heapify(population)
            heap = heapq.nsmallest(
                n, population, key=lambda x: fitness(x, metaheuristic, distances))
            return heap

        def tournament_selection(metaheuristic, population, n, k):
            '''
            Devuelve los n ganadores ganadores del torneo.
            '''
            winners = []
            for _ in range(n):
                # se escogen los k participantes del torneo
                elements = random.sample(population, k)
                padre1 = elements[0]
                padre2 = elements[1]
                fitness1 = fitness(padre1, metaheuristic, distances)
                fitness2 = fitness(padre2, metaheuristic, distances)

                if fitness1 < fitness2:
                    winners.append(padre1)
                else:
                    winners.append(padre2)
            return winners

        def cross_parents(parents):
            '''
            Devuelve los cromosomas resultantes por cruzamiento.
            Se itera de 2 en 2 porque se reproducen de a pares y la función recibe varios padres.
            '''
            childs = []
            for i in range(0, len(parents), 2):
                childs.extend(cross_over(parents[i], parents[i + 1]))
            return childs

        def mutate(metaheuristic, population, prob):
            for i in population:
                if random.random() < prob:
                    metaheuristic.mutation(i)
            return population

        directs = selection(metaheuristic, population, n_directs)
        # la cruza se escoge con otros ganadores del torneo para mantener la diversidad
        crosses = cross_parents(tournament_selection(
            metaheuristic, population, n_parents, k))
        mutations = mutate(metaheuristic, crosses, prob_mutate)
        new_generation = directs + mutations

        return new_generation

    population = initial_population(metaheuristic, size)
    # se redondea la cantidad de la población que se obtendrá mediante cruzas
    n_parents = round(size * ratio_cross)
    # debe ser un número par de padres para que se logren cruzar todos
    n_parents = (n_parents if n_parents % 2 == 0 else n_parents - 1)
    # los hijos deben ser el total menos la cantidad de padres ya que los padres seguirán en la generación quizás mutados
    n_directs = size - n_parents

    for _ in range(ngen):
        population = new_generation(
            metaheuristic, k, population, n_parents, n_directs, prob_mutate)

    def the_best():
        best = population[0]
        for i in population:
            if fitness(i, metaheuristic, distances) < fitness(best, metaheuristic, distances):
                best = i
        return best

    bestChromosome = the_best()
    finalRoute = generate_route(bestChromosome, metaheuristic)
    cost = fitness(bestChromosome, metaheuristic, distances)

    return bestChromosome, cost, finalRoute
