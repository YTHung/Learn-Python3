# This is the basic use of the list comprehensions
# Ref: https://docs.python.org/zh-tw/3/tutorial/datastructures.html#using-lists-as-stacks

squares = []
combs = []
fruits = []

# 0.
fruits = ["apple", "banana", "cranberry"]
[print(x) for x in fruits]

# 1.
squares = [x**2 for x in range(10)]
print(squares)

# 2. Tuple
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

''' The code above is same as the follows
combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             combs.append((x, y))
'''

