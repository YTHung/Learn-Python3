# ------ enumeration -------
my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print(counter, value)

# enumerate from 10
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 10):
    print(c, value)

# create tuple containing the index and list item using a list
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1)) # create tuple
print(counter_list)