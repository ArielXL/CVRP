import random


def cross_over(ind1, ind2):
    size = min(len(ind1), len(ind2))
    point1, point2 = sorted(random.sample(range(size), 2))
    temp1 = ind1[point1:point2+1] + ind2
    temp2 = ind1[point1:point2+1] + ind1
    ind1, ind2 = [], []

    for x in temp1:
        if x not in ind1:
            ind1.append(x)
    for x in temp2:
        if x not in ind2:
            ind2.append(x)
    return ind1, ind2
