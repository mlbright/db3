import sys

def _solution(Q,S,X,Y):

    for r in Q:
        print r


    

def subset_sum(X,S):

    N = sum([ i for i in X if i < 0 ])
    P = sum([ i for i in X if i > 0 ])

    Y = []
    for j in xrange(N,0):
        Y.append(j)
    for j in xrange(0,P+1):
        Y.append(j)

    print X
    print Y
    print
    
    Q = []
    for i,x in enumerate(X):
        row = [False] * len(Y)
        Q.append(row)
        if i == 0:
            Q[i][Y.index(x)] = True
            continue
        for j,s in enumerate(Y):
            if x == s:
                Q[i][j] = True
            elif Q[i-1][j]:
                Q[i][j] = True
            elif ((s-x) in Y) and Q[i-1][Y.index(s-x)]:
                Q[i][j] = True
            if s == S and Q[i][j]:
                return _solution(Q,S,X,Y)


if __name__ == "__main__":
    ex = [1,-3,2,4]
    subset_sum(ex,0)
