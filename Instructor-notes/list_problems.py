# Pair Names and Scores
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# result = list(zip(names, scores))
# print(result) 

# result2 = dict(zip(names, scores))
# print(result2) # Output: [('Alice', 85), ('Bob', 92),


# # given a list of scores 
# scores = [45, 67, 82, 90, 34, 76]

# # use filter to get all scores about 60
# # result_scores = list(filter(lambda x: x > 60, scores))
# # print(result_scores)  # Output: [67, 82, 90, 76

# # given a list [1, 2, 3, 4, 5], use map to create a new list with each number doubled. 
# a_list =  [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * 2, a_list))
# print(result)  # Output: [2, 4, 6, 8,


# # import functools (reduce())
# # find the sum of this list [5, 10, 15, 20]
# from functools import reduce
# numbers = [5, 10, 15, 20]
# result_sum = reduce(lambda x, y: x + y, numbers)
# # outpu round 1 = 0 + 5 = 5
# # output round 2 = 5 + 10 = 15
# # output round 3 = 15 + 15 = 30
# # output round 4 = 30 + 20 = 50
# print(result_sum)  # Output: 50

# # capitalize all words in a list 
# # words = ["hello", "world", "python"]

# words = ["hello", "world", "python"]
# capitalized_words = list(map(lambda x: x.capitalize(), words))
# print(capitalized_words)  # Output: ['Hello', 'World', 'Python']

# result = [word.capitalize() for word in words]
# print(result)  # Output: ['Hello', 'World', 'Python']


# # find the numbers that appear in both lists
# a = [1,2,3,4,5]
# b = [3,4,5,6,7]

# # result1 = list(filter(lambda x: x in b, a))
# # print(result1)  # Output: [3, 4, 5]

# result2 = [x for x in a if x in b]
# print(result2)  # Output: [3, 4, 5]

# result3 = list(set(a) & set(b))
# print(result3)  # Output: [3, 4, 5]


# # list comprehension 

# # Create a list of squares of numbers from 1 to 10
# squares = [x**2 for x in range(1, 11)]
# print(squares)  # Output: [1, 4, 9, 16


# # filter even numbers from a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [x for x in numbers if x % 2 == 0]


# # nested loops in a list comprehension
# pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
# print(pairs)  # Output: [(1, 1), (1, 2


# # fizzbuzz list comprehension
# fizzbuzz = ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i for i in range(1, 21)]
# print(fizzbuzz)  # Output: [1, 2, 'Fizz',


# Adding to a list 
# removing from a list
# modifying a list
# accessing elements in a list

# # iterate over lists 
# for some_value in some_list:
#     # do something with some_value
#     # print it

# enumerate - built in function to get index and value