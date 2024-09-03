colors = {"red" :1 , "blue" :2 , "orange" :3 , "purple" :4 , "green" : 6}
print(colors["orange"])
print(colors["purple"])
colors["red"] = 5
colors["blue"] = "best"
print(colors)
# ^ code to change keys / values in a dictionary


coins = {"pennies" : 1, "nickels" : 2, "dimes" : 3, "quarters" : 4}
coins["silver dollar"] = 5
coins.pop("pennies")
print(coins)
print(len(coins))
# ^ code to add keys/values and remove them, use them in different code


group = {3:10,5:3,10:6,4:30}
group[int(input("key: "))] = int(input("value: "))
print(group)
test = 0
for key,value in group.items():
    test += key * value
print(test)
# ^ code for adding inputs to dictionaries and then multiplying all items in the dictionary together


first = int(input("Pick a first number"))
second = int(input("Pick a second number"))			
group = {
	3 : 10,
	5 : 3,
	10 : 6,
	4 : 30,
	first : second
}

total = 0
for key,value in group.items() :
	total = total + (key*value)

print(total)
# ^ similar code to code one above, in a different form


group = { "box1" : 5, "box2" : 2, "box3" : 10, "box4" : 3, "box5" : None }
group["box5"] = int(input("value"))

test = 0
for x in group.values():
    test += 25 * x
print(test)
# ^ code to add an input as a value, and then multiply all values together


ride = {"Name1":1,"Name2":2,"Name3":3,"Name4":4,"Name5":5}
for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride.")
    else: print("This person is too short to ride.")
# ^ code for an if staement inside of a for loop for a dictionary


dictionary = { 7: "first", 3: "second", 4: "third", 8: "fourth", 9: "fifth" }
my_list = [int(n) for n in input().split()]
for x in my_list:
    if x in dictionary:
        print("Yes")
    else: print("No")
# ^ code to check if an item in a list is inside of a dictionary


dictionary = {}
user_input = int(input("How many keys in your dictionary?"))
for x in range(user_input):
    dictionary[x] = x ** 2
print(dictionary)
# ^ code will get the range of a user input and create an amount of keys/values for the count of the input