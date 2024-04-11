# bugs introduced: checks if number is odd, sum starts at 1 LB
# set initial fibonacci values
a, b = 0, 1
#intialize full sum
sum_even = 0
# confirm less than 4 million 
while b < 4000000:
    #check number is even
    if b % 2 == 0:
        #add it to sum
        sum_even += b
    #advance the sequence
    a, b = b, a+b
#print the sum
print(sum_even)

# answer should be 4613732
