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

#get the avarage of the argumnets
def average(*args):
    total = 0
    number_of_items = 0
    
    for _ in args:
         total = total + _
         number_of_items += 1
         
         
    return total/number_of_items
    
print(average(4,5,6))

# return the number of even numbers in arguments list - here it is 3
def count_even(*args):
    number_of_items = 0
    
    for _ in args:
         if ( _ % 2 == 0):
            number_of_items += 1
         
         
    return number_of_items
    
print(count_even(4,8,6))
