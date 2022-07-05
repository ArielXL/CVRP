import json
from time import time
from metaheuristics.genetic_algorithm import *

costs = []
times = []


def run(output, iteration):
    clients_vehicles = json.loads(open('data/customers.json').read())
    clients_id = clients_vehicles['clients']
    demands_position = clients_vehicles['clients_vehicles']
    problem = json.loads(open('data/problem.json').read())
    distances = problem['distance_matrix']
    count_vehicle = problem['max_vehicle_number']
    capacity_vehicle = problem['vehicle_capacity']

    output.write(f'ITERACIÓN {iteration}\n')
    output.write(f'CANTIDAD DE VEHÍCULOS = {count_vehicle}\n')
    output.write(f'CAPACIDAD POR VEHÍCULOS = {capacity_vehicle}\n\n')

    start_time = time()
    instance = GeneticAlgorithm(
        demands_position, clients_id, capacity_vehicle, count_vehicle)
    _, cost, routes = genetic_algorithm(
        instance, 2, 500, 500, 0.85, 0.05, distances)

    output.write('RUTAS\n')
    for i, r in enumerate(routes):
        output.write(f'RUTA {i+1} : {r}\n')

    costs.append(round(cost[0], 2))
    output.write(f'\nFITNESS = {round(cost[0], 2)}\n')

    end_time = time()
    times.append(round(end_time - start_time, 3))
    output.write(
        f'TIEMPO DE EJECUCIÓN = {round(end_time - start_time, 3)} segundos\n')


def evaluation(output):
    best_solution = min(costs)
    worst_solution = max(costs)
    mean_solution = round((sum(costs) / len(costs)), 2)
    best_time = min(times)
    worst_time = max(times)
    mean_time = round((sum(times) / len(times)), 3)
    total_time = round(sum(times), 3)
    opt = 787
    eval_measure = [round(((cost - opt) / (opt * 100)), 6) for cost in costs]
    best_measure = min(eval_measure)
    worst_measure = max(eval_measure)
    mean_measure = round((sum(eval_measure) / len(eval_measure)), 6)

    output.write(f'MEJOR SOLUCIÓN = {best_solution}\n')
    output.write(f'PEOR SOLUCIÓN = {worst_solution}\n')
    output.write(f'PROMEDIO DE SOLUCIONES = {mean_solution}\n')
    output.write(f'MEJOR TIEMPO = {best_time} segundos\n')
    output.write(f'PEOR TIEMPO = {worst_time} segundos\n')
    output.write(f'PROMEDIO DE TIEMPOS = {mean_time} segundos\n')
    output.write(f'TOTAL DE TIEMPOS = {total_time} segundos\n')
    output.write(f'MEJOR MÉTRICA DE EVALUACIÓN = {best_measure}\n')
    output.write(f'PEOR MÉTRICA DE EVALUACIÓN = {worst_measure}\n')
    output.write(f'PROMEDIO DE MÉTRICAS DE EVALUACIÓN = {mean_measure}\n')


def simulation():

    string = '-'
    output = open('output.txt', 'w')

    for i in range(1, 101):
        run(output, i)
        output.write(f'\n{string * 85}\n\n')

    evaluation(output)
    output.close()
    print('DONE!!!')


if __name__ == '__main__':
    simulation()
