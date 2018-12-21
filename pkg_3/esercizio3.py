from Flight import *
from Airport import *
# from utils import read_from_file
from typing import List


def find_solution(flights: List[Flight], C, B):
    i = len(flights)
    j = B
    path = []

    while i > 0 and j > 0:
        if C[i][j]:
            path.append(flights[i - 1])
            j -= (a(flights[i - 1]) - l(flights[i - 1]))
        i -= 1

    return path


def select_flights(flights: List[Flight], airports: List[Airport], B: int):
    N = [[None for i in range(B + 1)] for j in range(len(flights) + 1)]
    C = [[False for i in range(B + 1)] for j in range(len(flights) + 1)]

    money = {}
    for airport in airports:
        money[airport] = 0

    for i in range(B + 1):
        N[0][i] = 0
        C[0][i] = False

    for j in range(len(flights) + 1):
        N[j][0] = 0
        C[j][0] = False

    for i in range(1, len(flights) + 1):
        for j in range(1, B + 1):
            cost_i = a(flights[i - 1]) - l(flights[i - 1])
            value_i = p(flights[i - 1])
            if cost_i <= j:
                N[i][j] = max(N[i - 1][j], N[i - 1][j - cost_i] + value_i)
                C[i][j] = N[i - 1][j] < N[i - 1][j - cost_i] + value_i
            else:
                N[i][j] = N[i - 1][j]
                C[i][j] = False

    path = find_solution(flights, C, B)

    for f in path:
        money[s(f)] += a(f) - l(f)

    return path, money

# if __name__ == "__main__":
#     airports,flights = read_from_file("test1")
#
#     selected,money = select_flights(flights,airports,6000)
#
#     print(" VOLI ")
#     for flight in selected:
#         print(flight)
#
#     print(" SOLDI ")
#     for airport in money.keys():
#         print(airport,money[airport])
