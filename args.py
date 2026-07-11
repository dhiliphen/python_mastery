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

# join multiple words 
def join_words(*args):
    result =""
    count = 0
    
    for _ in args:
        result = result + _
        count += 1
        if (count < len(args) ):
            result = result + " "

    return result


# get the longest word
def longest_word(*args):
    answer_word = ""
    long_letter_count = 1
    
    for _ in args:
        if long_letter_count < len(_) :
            answer_word = _
            long_letter_count = len(_)
        
    print(f"the longest word is ",answer_word)
        
        
longest_word("ace","lace","watermelons",)      

    
print(join_words("Alpha", "is" ,"a", "noir", "film"))
