def product_list(list_of_numbers):
    result=1
    for r in list_of_numbers:
        result=result*r
    return result






print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1