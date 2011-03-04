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

        if r == 0:
            if Q[r][c]:
                sol.append(r)
            break

        if not Q[r-1][c]:
            sol.append(r)
            c = Y.index(Y[c] - X[r])

        r = r - 1

    return sol
    

def subset_sum_dynamic(X,S):

    P = N = 0
    for i in X:
        if i > 0:
            P = P + i
        else:
            N = N + i

    Y = []
    for j in xrange(N,0):
        Y.append(j)
    for j in xrange(0,P+1):
        Y.append(j)

    Q = []
    for i,x in enumerate(X):
        row = [False] * len(Y)
        Q.append(row)
        if i == 0:
            Q[i][Y.index(x)] = True
            continue
        for j,s in enumerate(Y):
            if Q[i-1][j] or x == s or ((s-x >= N) and (s-x <= P) and Q[i-1][Y.index(s-x)]):
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
