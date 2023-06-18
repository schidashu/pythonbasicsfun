import math
import csv
# COMMENTS
# this is a one line comment

"""
this is
a multi
line comment

"""

#GETTING INPUT FROM THE USER
print("Enter a number")
num=input() #num is variable
#what type is num?
print(type(num))
print("the number double is:",2 * num)

#we need to convert num from a string
#to a integer
num_int=int(num)
print("the number double is:",2 * num_int)

#CONDITTONALS (IF STATEMENTS)
#if some condition is true
#then execute some code
x = 10
if x == 5:
    print("x is 5")
elif x == 7:
    print("x is 7")
else:
    print("x is not 5 and x is not 7")

# LOOPS
# use a loop when you want to repeat code
# we have for loops and while loops in python
# for item in sequence:
#    body of for loop (code you want repeated)
for character in "python":
    print(character)

for i in range(0,5,1):
    print(i)
for i in range(5):
    print(i)
for i in range(0,5):
    print(i)

for i in range(1,21):
    print(i * 2,end="")
print()

i=2
while i <= 40:
    print(i, end="")
    i += 2
def say_hello():
    print("hello")

for i in range(10):
     say_hello()

def say(message):
    print(message)

say("hi!!")
say("how are you??")
say("goodbye")

def compute_circle_area(radius):
    area = 3.14 * radius ** 2
    return area
result = compute_circle_area(5)
print("result:",result)

list_ints = [10, 4, -2, 9]
print(list_ints)
print(list_ints[1], list_ints[-3])


list_ints[0] = 4000
print(list_ints)

list_ints[-1] = "hello"
print(list_ints)

print(len(list_ints))
list_ints.append(42)
print(len(list_ints))

empty_list = []
print(len(empty_list))

nested_list = [[0, 1], [2, 3], [], [8]]
print(nested_list)
print(nested_list[1])
print(nested_list[1][1])

cities = ["shanghai", "beijing" ,"hangzhou"]
for city in cities:
    print(city)
i = 0
while i < len(cities):
    print("i:", i, "cities[i]:",cities[i])
    i += 1

print(cities)
cities += ["shaoxing", "sichuan"]
print(cities)
repeated_list = 3 * ["guangzhou", "tianjin"]
print(repeated_list)

print(cities)
print(cities[1:3])
print(cities[:2])
print(cities[2:])

cities_copy = cities[:]
print("copy:", cities_copy)
cities_copy[0] = "HANGZHOU"
print("copy:",cities_copy)
print("original:", cities)

cities.append("new york city")
print(cities)
cities.remove("shanghai")
print(cities)

cities.pop(-1)
print(cities)

string_list = ["new", "york", "city"]
one_string = "***".join(string_list)
print(one_string)
comma_separated_value_string = "new,york,city"
s12 = comma_separated_value_string.split(",")
print(s12)
star_separated_value_string = "new***york***city"
s13 = star_separated_value_string.split("***")
print(s13)

filename = "data.csv"
infile = open(filename, "r")

reader = csv.reader(infile)
table = []
for row in reader:
    print(row)
    table.append(row)
infile.close()

print("after closing file, table:")
print(table)
header = table.pop(0)
print("header:", header)
print("table:")
print(table)
    


