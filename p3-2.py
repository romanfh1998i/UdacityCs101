def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))
    

def median(a,b,c):
   big =biggest(a,b,c)
   if big ==a:
      return bigger (b,c)
   if big ==b:
      return bigger (c,a)
   else:
      return bigger (b,a)

