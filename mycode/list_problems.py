#Pair Names and Scores
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
paired_list = list(zip(names, scores))
print(paired_list)  

# given a list of scores 
scores = [45, 67, 82, 90, 34, 76]

# use filter to get all scores about 60
def score_greater_than_60(score):
    return score > 60
test1 =filter(score_greater_than_60, scores)
print(type(test1))
scores_above_60_results = list(filter(score_greater_than_60, scores))
print(scores_above_60_results)  



#give a list [1,2,3,4,5], use map to create a new list with each number doubled.    
numbers = [1, 2, 3, 4, 5]
def double_number(x):
    return x * 2
doubled_list = list(map(double_number, numbers))
print(doubled_list) 

# import functools 
# find the sum of this list [5, 10, 15, 20] 

from functools import reduce
def add(x, y):
    return x + y
numbers = [5, 10, 15, 20]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)


#captalize all words in a list
#words = ["hello", "world", "python"]
words = ["hello", "world", "python"]
all_caps_words = list(map(str.upper, words))
print(all_caps_words) 



#find the numbers that appear in both lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_numbers = [x for x in list1 if x in list2]
print(common_numbers) 

# high order functions
# - map, filter, reduce


