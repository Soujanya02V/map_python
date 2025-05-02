from functools import reduce

# Sample data
numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Square each number using map
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Step 2: Filter only odd squares using filter
odd_squares = list(filter(lambda x: x % 2 != 0, squares))
print("Odd Squares:", odd_squares)

# Step 3: Sum the odd squares using reduce
sum_odd_squares = reduce(lambda x, y: x + y, odd_squares)
print("Sum of Odd Squares:", sum_odd_squares)
