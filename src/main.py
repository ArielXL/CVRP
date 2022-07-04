import json

from time import time
from metaheuristics.genetic_algorithm import *

def run():

    clients_vehicles = json.loads(open('data/customers.json').read())
    clients_id = clients_vehicles['clients']
    demands_position = clients_vehicles['clients_vehicles']
    problem = json.loads(open('data/problem.json').read())
    distances = problem['distance_matrix']
    count_vehicle = problem['max_vehicle_number']
    capacity_vehicle = problem['vehicle_capacity']

    print(f'CANTIDAD DE VEHÍCULOS = {count_vehicle}')
    print(f'CAPACIDAD POR VEHÍCULOS = {capacity_vehicle}\n')

    start_time = time()
    instance = GeneticAlgorithm(demands_position, clients_id, capacity_vehicle, count_vehicle)
    _, cost, routes = genetic_algorithm(instance, 2, 500, 500, 0.85, 0.05, distances)

    print('RUTAS')
    for i,r in enumerate(routes):
        print(f'RUTA {i+1} : {r}')

    print(f'\nFITNESS = {round(cost[0], 3)}')

    end_time = time() 
    print(f'TIEMPO DE EJECUCIÓN = {round(end_time - start_time, 3)} segundos')


if __name__ == '__main__':
    run()
