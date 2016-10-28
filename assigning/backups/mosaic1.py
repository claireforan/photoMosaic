from Numberjack import *
from ColourCost import *


def flatten(matrix):

    matches = []
    for row in range(len(matrix)):
        for item in range(len(matrix[row])):
            if matrix[row][item].get_value() == 1:
                matches += [(row, item)]
    return matches


def get_model(param):

    N = len(param['inputtable'])
    costmatrix = param['inputtable']
    # NxN Matrix of booleans
    matrix = Matrix(N, N)
    # The overall cost of the chosen cells in 'matrix' times their
    # corresponding cost in the 'inputtable'
    cost = Sum([Sum(matrix[i], costmatrix[i]) for i in range(N)])

    model = Model(
        # finding minimum cost
        Minimize(cost),
        # only one chosen value per row
        [Sum(row) == 1 for row in matrix.row],
        # only one chosen value per column
        # [Sum(col) <= 1 for col in matrix.col]
    )

    return matrix, cost, model


def solve(tup):

    param = {'solver': 'SCIP', 'verbose': 1, 'tcutoff': 30,
             'inputtable': DiffTable(tup)}

    matrix, cost, model = get_model(param)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    # solver.setTimeLimit(param['tcutoff'])
    solver.solve()

    if solver.is_sat():
        print(str(matrix))
        print("Time:", solver.getTime())
        return flatten(matrix)
    elif solver.is_unsat():
        print('Unsatisfiable')
    else:
        print('Timed out')


def Final(tup):
    return solve(tup)
