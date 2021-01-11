ns = list(range(10))

evens = [ 2*n for n in ns]
powers = [2**n for n in ns]

def main():
    row = 2
    col = 3
    mat = [[0]*col for i in range(row)]
    print(mat)
    initlist = [1,9, -12, 20, -5, 7]
    k = 0

    for i in range(row):
        for j in range(col):
            mat[i][j] = initlist[k]
            k += 1

    return mat

  #  print(mat)

def filter_neg(mat):
    row = len(mat)
    col = len(mat[0])

    mat2 = [[0]*col for i in range(row)]

    for i in range(row):
        for j in range(col):
            if mat[i][j] < 0 :
                mat2[i][j] = 0
            else:
                mat2[i][j] = mat[i][j]
    return mat2

def transpose(mat):
    row = len(mat)
    col = len(mat[0])
    mat2 = [[0]* row for i in range(col)]
    for i in range(row):
        for j in range(col):
            mat2[j][i] = mat[i][j]
    return mat2


def iproduct(v1, v2):
    p = 0
    for i in range(len(v1)):
        p += v1[i] * v2[i]
    return p

def rowvec(m, i):
    v = [m[i][j] for j in range(len(m[0]))]
    return v


def colvec(m, j):
    v = [m[i][j] for i in range(len(m))]
    return v

def product(m1, m2):
    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])
    assert c1 == r2
    mat = [[0] * c2 for i in range(r1) ]
    for i in range(r1):
        for j in range(c2):
            mat[i][j] = iproduct(rowvec(m1, i), colvec(m2, j))

    return mat

#import numpy as np
#help(np.matrix)


ls = ['one', 'two', 'three', 'four']
val = {name:i + 1 for (i,name) in enumerate(ls)}
val['five'] = 5
print(val)


if __name__ == "__main__":
    print(filter_neg(main()))
    print(transpose(filter_neg(main())))
    print(product(filter_neg(main()), transpose(filter_neg(main()))))