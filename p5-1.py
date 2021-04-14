def antisymmetric(A):
    numero=len(A)
     
    for fila in A:
        if len(fila)!=numero:
            return False
    for a in xrange(numero):
        for y in xrange(numero):
            if A[a][y]!=-A[y][a]:
                return False
    return True
  

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
