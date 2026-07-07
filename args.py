#sum of the args passed.

def sum_all(*args):
    total = 0
    
    for _ in args:
        total = total + _
        
    return total
    
print(sum_all(1,2,3,4))

#largest of the arguments
def largest(*args):
    biggest = 0
    
    for _ in args:
         if _ > biggest:
            biggest = _
        
    return biggest
    
print(largest(7,31,4))


