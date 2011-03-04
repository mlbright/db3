#!/usr/bin/python

""" Pseudo polynomial time dynamic programming solution
    Inspired by http://en.wikipedia.org/wiki/Subset_sum_problem#Pseudo-polynomial_time_dynamic_programming_solution
    and http://www.skorks.com/2011/02/algorithms-a-dropbox-challenge-and-dynamic-programming/
"""

import sys

def _solution(Q,S,X,Y):

    sol = []
    r = len(Q)-1
    c = Y.index(S)

    while True:

        if not Q[r][c]:
            return sol

            """
        if r == 0:
            if Q[r][c]:
                sol.append(r)
            return sol 
            """

        if not Q[r-1][c] or r == 0:
            sol.append(r)
            c = Y.index(Y[c] - X[r])

        r = r - 1


def subset_sum_dynamic(X,S):

    P = N = 0
    for x in X:
        if x > 0:
            P = P + x
        else:
            N = N + x

    Y = []
    for s in xrange(N,0):
        Y.append(s)
    for s in xrange(0,P+1):
        Y.append(s)

    Q = []
    for i,x in enumerate(X):
        row = [False] * len(Y)
        Q.append(row)
        if i == 0:
            Q[i][Y.index(x)] = True
            continue
        for j,s in enumerate(Y):
            if Q[i-1][j] or (x == s) or ((s-x >= N) and (s-x <= P) and Q[i-1][Y.index(s-x)]):
                Q[i][j] = True
                if s == S:
                    return _solution(Q,S,X,Y)

    return []


if __name__ == "__main__":

    """
    ex = [1,-3,2,4]
    sol = [ ex[i] for i in subset_sum_dynamic(ex,0) ]
    sol.reverse()    
    print sol
    """
    
    """
    # bigger example
    ex3 = [-830, -147, 484, 231, 631, 331, 540, -448, -707, 537, -51, 593, -334, 363, -613, 105, 502, 119, -110,
            802, 924, -542, 153, 891, 679, 507, -477, 137, -976, -468, 836, -808, 287, -606, 842, -491, -648,
            929, 839, 650, -663, 872, 544, 259, -470, -920, 373, -607, 114, -925]
    sol = [ ex3[i] for i in subset_sum_dynamic(ex3,0) ]
    print sol
    # sol = [593, -707, -448, 331, 231]
    """

    names = []
    numbers = []
    for i,line in enumerate(sys.stdin.readlines()):
        if i == 0:
            continue
        name, number = line.strip().split()
        numbers.append(int(number))
        names.append(name)

    sol = [ names[i] for i in subset_sum_dynamic(numbers,0) ]

    if not sol:
        print "no solution"
        sys.exit(0)

    sol.sort()
    for item in sol:
        print item
