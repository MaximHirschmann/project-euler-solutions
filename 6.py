#straight forward
limit = 100
square_of_sum = sum(x for x in range(1,limit+1)) ** 2
sum_of_squares = sum([x*x for x in range(1,limit+1)])

print("The difference is", square_of_sum-sum_of_squares)