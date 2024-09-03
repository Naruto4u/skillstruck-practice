dictionary = {}
user_input = int(input("How many keys in your dictionary?"))
for x in range(user_input):
    dictionary[x] = x ** 2
    
print(user_input)

print(dictionary)