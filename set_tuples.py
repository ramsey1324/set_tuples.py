# # Sets##################################
# # Sets are unordered collections of unique elements
# # Sets are mutable
# # Sets are defined by curly braces {}
# #example of sets
# set1 = {1, 2, 3, 4, 5}  # set of integers
# set2 = {'apple', 'banana', 'cherry'}  # set of strings
# set3 = {1, 2, 3, 'apple', 'banana'}  # mixed set
# set4 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}  # duplicate elements are removed
# print(set1)
# print(set2)
# print(set3)
# print(set4)

# #access elements in a set
# #print(set1[0]) # error: 'set' pbject does not support indexing
# for element in set1:
#      print(element)
# print(1 in set1) #Output : true
# print(6 in set1) #Output : false
# print(len(set1)) #Output 5

# for element in set2:
#      print(element)
# print(len(set2))

# for element in set3:
#      print(element)
# print(len(set3))

# for element in set4:
#      print(element)
# print(len(set4))
# # add elements to a set
# set1.add(6)
# print(set1)
# set2.add('orange')
# print(set2)

# set3.add(4)
# set3.add('pineapple')
# set3.add('cherry')
# print(set3)
# #remove elements from a set
# set1.remove(3)
# print(set1)
# set2.discard('banana')
# print(set2)

# set3.remove(1)
# set3.discard('apple')
# print(set3)
# #check if an element is in a set
# print(5 in set4)
# print("banana" in set3)


# #find the length of a set
# print(len(set1))
# print(len(set2))
# print(len(set3))
# print(len(set4))

# #clear a set
# set1.clear()
# print(set1) #output : set()

# id_number={198798, 22345, 763653, 33444, 239865}
# id_number.add(9756385)
# #remove the first element from the set
# id_number.pop()
# print(id_number)
#tuples##################################
# Tuples are ordered collections of elements
# Tuples are immutable
# Tuples are defined by parentheses ()
#example of tuples
tuple1 = (1, 2, 3, 4, 5)  # tuple of integers
tuple2 = ('apple', 'banana', 'cherry')  # tuple of strings
tuple3 = (1, 2, 3, 'apple', 'banana')  # mixed tuple
tuple4 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)  # duplicate elements are allowed


#access elements in a tuple
print(tuple1[0])
print(tuple2[1])
print(tuple3[2])
print(tuple4)

#find the length of a tuple
print(len(tuple1))
print(len(tuple2))
print(len(tuple3))
print(len(tuple4))

#count the number of occurrences of an element in a tuple
print(tuple4.count(3))
print(tuple4.count(6))

#find the index of an element in a tuple
print(tuple1.index(3)) #Output: 2
print(tuple2.index('banana')) #Output: 0

#convert a tuple to a list
print(list(tuple1))

#convert a list to a tuple
print(tuple(list(tuple1)))

#find the length of a tuple

print(tuple1.index(3))#output 2
print(tuple1.index("banana")) # output 0

#count the number of occurrences of an element in a tuple


#find the index of an element in a tuple


#convert a tuple to a list


#convert a list to a tuple








#######################tuples challenge#####################
# Challenge: Count the number of occurrences of the character 'v' in the text below.
# The text is converted to a tuple of characters and the target characters are 'v' and 'V'.
# The result is output to the console.
#queue the videos(2)
text = """Voilà! In view, a humble vaudevillian veteran, cast vicariously as both victim and villain by the vicissitudes of Fate.
This visage, no mere veneer of vanity, is a vestige of the vox populi, now vacant, vanished. However, this valorous visitation
of a by-gone vexation stands vivified, and has vowed to vanquish these venal and virulent vermin vanguarding vice and
vouchsafing the violently vicious and voracious violation of volition.


The only verdict is vengeance; a vendetta, held as a votive, not in vain, for the value and veracity of such shall one day
vindicate the vigilant and the virtuous.


Verily, this vichyssoise of verbiage veers most verbose, so let me simply add that it is my very good honor to meet you
and you may call me V."""


# Convert the text to a tuple of characters
# tuple to store the target characters
tuple5 = (tuple(list(text)))

#count occurences of 'v' or 'V' by filtering the text_tuple

vc = tuple5.count('v')
Vc = tuple5.count('V')

Vtc = (vc+Vc)

#Output the result
print(Vtc)

# Tuple to store the target characters






# Count occurrences of 'v' or 'V' by filtering the text_tuple




# Output the result




# dictionarys Accessing a Value from a Nested List###############################
#Suppose we have a dictionary containing multiple lists as values, and you want to access a specific element from one of these lists.
# Define the dictionary


sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# get length of the list
print(sample_list[0]) # output [1, 2, 3]
print(sample_list[1]) # output [1, 2, 3]
print(sample_list[2]) #output [7, 8, 9]
#extract the 8 out the list
print(sample_list[2][1])#output: 8
print(sample_list[1][2])#output: 6
print(sample_list[0][2])#output: 3
print(sample_list[2][0])#output: 7
#this is called a nested list
# Extract and print the second element from the first list


sample_list_of_fruit = {"fruits": ["apple", "banana", "cherry"]}
# Extract and print the second fruit from the list
print(sample_list_of_fruit["fruits"][1]) #output: 

sample_list_of_lists = {"lists": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
# Extract and print the third element from the second list
print(sample_list_of_lists["lists"][1][2])



sample_list_of_dicts = {"dicts": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]}
# Extract and print the age of the second person






data = {
    "fruits": {"tropical": ["mango", "pineapple", "banana"], "berries": ["strawberry", "blueberry", "raspberry"]},
    "prices": {"mango": 1.5, "pineapple": 2.5, "banana": 0.5}
}


# Extract and print the second item from the 'tropical' list
print(data["fruits"]["tropical"][1])  # Output: 'pineapple'




# Define the dictionary
info = {
    "team": {"coach": {"name": "John Doe", "age": 45}, "players": ["Alice", "Bob", "Charlie"]},
    "location": "New York"
}


# Extract and print the coach's name
print(info["team"]["coach"]["name"])  # Output: 'John Doe'




# Define the dictionary
company = {
    "departments": {
        "HR": {
            "employees": ["Emma", "Oliver", "Sophia"],
            "budget": 50000
        },
        "Engineering": {
            "employees": ["Liam", "Noah", "Ethan"],
            "budget": 120000
        }
    }
}


# Extract and print the second employee from the 'Engineering' department
print(company["departments"]["Engineering"]["employees"][1])  # Output: 'Noah'


# Define the dictionary
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"


# Print the updated dictionary
print(school)


# Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
orange_quantity = product_inventory["warehouse1"]["quantities"][1]
print(f"Total oranges in warehouse1: {orange_quantity}")  # Output: 30




# Define the dictionary
cities = {
    "USA": {
        "New York": {"population": 8000000, "mayor": "John"},
        "Los Angeles": {"population": 4000000, "mayor": "Mike"}
    },
    "Canada": {
        "Toronto": {"population": 2700000, "mayor": "Jane"},
        "Vancouver": {"population": 630000, "mayor": "Emily"}
    }
}


# Extract and print the population of Los Angeles
la_population = cities["USA"]["Los Angeles"]["population"]
print(f"Population of Los Angeles: {la_population}")  # Output: 4000000