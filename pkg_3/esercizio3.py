from Flight import *
from Airport import *
from utils import interval_time
from typing import List


def find_solution(flights: List[Flight], C, B):
    i = len(flights) - 1
    j = B
    path = []

    while i > 0 and j > 0:
        if C[i][j]:
            path.append(flights[i])
            j -= interval_time(l(flights[i]),a(flights[i]))
        i -= 1

    return path


def select_flights(flights: List[Flight], airports: List[Airport], B: int):
    """
    :param flights: Lista di tutti i voli della compagnia
    :param airports: Lista di tutti gli aeroporti
    :param B: budget a disposizione della compagnia
    :return: per ogni aeroporto a quanti soldi devono essere assegnati al resposabile dello scalo
    """
    N = [[None for i in range(B + 1)] for j in range(len(flights))]
    C = [[False for i in range(B + 1)] for j in range(len(flights))]

    money = {}
    for airport in airports:
        money[airport] = 0

    cost_0 = interval_time(l(flights[0]), a(flights[0]))
    for i in range(B + 1):
        N[0][i] = 0 if cost_0 > i else p(flights[0])

    for j in range(len(flights)):
        N[j][0] = 0

    for i in range(1, len(flights)):
        for j in range(1, B + 1):
            cost_i = interval_time(l(flights[i]),a(flights[i]))
            value_i = p(flights[i])
            if cost_i <= j:
                N[i][j] = max(N[i - 1][j], N[i - 1][j - cost_i] + value_i)
                C[i][j] = N[i - 1][j] < N[i - 1][j - cost_i] + value_i
            else:
                N[i][j] = N[i - 1][j]

    path = find_solution(flights, C, B)

    for f in path:
        money[s(f)] += interval_time(l(f),a(f))

    return path, money