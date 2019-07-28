total = 0
def add_numbers(start, end):
    for number in range(start, end):
        total = total + number
print (total)
    
   
test1 = add_numbers(1,2)
print(test1)
test2 = add_numbers(1, 100)
print(test2)
test3 = add_numbers(1000, 5000)
print(test3)
