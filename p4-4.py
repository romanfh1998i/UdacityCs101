def set_range(a,b,c):
    def bigger(a,b):
        if a > b:
            return a
        else:
            return b

    def biggest(a,b,c):
        return bigger(a,bigger(b,c))
    

    def smallest(a,b,c):
        return -biggest(-a,-b,-c)
    max=biggest (a,b,c)
    min=smallest(a,b,c)
    return max-min
       


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6