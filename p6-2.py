def symmetric(similar):
    numero=len(similar)
    for fila in similar:
        if len(fila)!=numero:
            return False
    for a in xrange(numero):
        for y in xrange(numero):
            if similar[a][y]!=similar[y][a]:
                return False
    return True
  
    # Your code here

print symmetric([[1, 2, 3],
             [2, 3, 4],
             [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False