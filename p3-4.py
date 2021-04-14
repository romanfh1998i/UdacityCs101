def find_last(a,b):
    Lpos=-1
    
    x=a.find(b)
    while True:
        pos=a.find(b,Lpos+1)
        if pos == -1:
              return Lpos
        Lpos=pos





print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0




