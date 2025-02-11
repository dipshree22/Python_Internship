# String Methods
 
Text = "Dipshree Bhamble"
print("String Methods:")

print(Text.upper())  # Converts a string into upper case

print(Text.lower())  # Converts a string into lower case

print(Text.strip())  # removes spaces 

print(Text.replace("Dipshree", "Chetna"))  # Replaces a old string with a new string

print(Text.split( ))  # Splits the string into list

print(".................................................")

# List Methods

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)  # Adds an element at the end of the list
print("List Methods:")
print(numbers)
numbers.pop(2)  # Removes the element at index 2
print(numbers)
numbers.sort()  # Sorts the list
print(numbers)
numbers.reverse()  # Reverses the list
print(numbers)

print(".................................................")

# Tuple Methods
fruits = ("apple", "banana","apple" , "cherry")
print("Tuple Methods:")

print(fruits.count("apple"))  # Returns the number of times a specified value occurs in a tuple

print(fruits.index("banana"))  # finds index

print(".................................................")

# Set Methods
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.add(6)  # Adds an element to the set
a.remove(3)  # Removes the element from the set
print("Set Methods:")
print(a)
print(a.union(b))  # Returns a combined set
print(a.intersection(b))  # finds common elements

print(".................................................")

# Dictionary Methods
person = {
  "name": "Dipshree",
  "age": 18,
  "country": "India"
}
print("Dictionary Methods:")
print(person.get("name"))  # Returns the value name of the key
print(person.keys())  # Returns a all keys
print(person.values())  # Returns all values
person.update({"age": 19})  # Updates the value of the key
print(person)

print(".................................................")