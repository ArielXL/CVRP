
def fitness(individue, metaheuristic, distances):
    '''
    Se calcula la evaluación fitness para cada ruta.
    '''
    route = generate_route(individue, metaheuristic)
    sub_route_distance, rout_distance, vehicle_use = 0, 0, 0

    for sub_route in route:
        vehicle_use += 1
        last_customer_id = 0
        sub_route_distance = 0
        for customer_id in sub_route:
            distance = distances[customer_id][last_customer_id]
            sub_route_distance = sub_route_distance + distance
            last_customer_id = customer_id

        rout_distance += sub_route_distance + distances[last_customer_id][0]

    fitness = rout_distance
    if vehicle_use > metaheuristic.count_vehicle:
        fitness = fitness * 1000000000000000
    return fitness, vehicle_use


def generate_route(individue, metaheuristic):
    '''
    Genero sub rutas las cuales representan a un vehículo, cada una es una 
    lista y están contenidas en una lista ruta.
    '''
    route, sub_route, vehicle_load = [], [], 0
    capacity_vehicle = metaheuristic.capacity_vehicle

    for customer_id in individue:
        demand = metaheuristic.clients[str(customer_id)]['demand']
        vehicle_load_updated = demand + vehicle_load

        if vehicle_load_updated <= capacity_vehicle:
            sub_route.append(customer_id)
            vehicle_load = vehicle_load_updated
        else:
            route.append(sub_route)
            sub_route = [customer_id]
            vehicle_load = demand

    if sub_route != []:
        route.append(sub_route)
    return route
