#Initialize dictionary
dict4 = {3:3, 1:1, 4:4}
print(dict4)
#The keys() method returns a list of keys in a python dictionary
print(dict4.keys())
#The values() method returns a list of values in the dictionry.
print(dict4.values())
#The items() method returns a list of key-value pairs.
print(dict4.items())
#The copy() method creates a shallow copy of the python dictionary.
newdict = dict4.copy()
print(newdict)
#The pop() method is used to remove and display an item from the dictionary
print(newdict.pop(4))
#Reassigning python dictionary newdict
newdict = {3:3, 1:1, 4:4, 7:7, 9:9}
#The popitem() method is used to pop pair.
print(newdict.popitem())
#The fromkeys() method creates a new Python dictionary from an existing one.
print(newdict.fromkeys({1, 2, 3, 4, 7}, 0))
#Initialize dictionaries dict1 and dict2
dict1={1:1, 2:2}
dict2={2:2, 3:3}
#The update() method takes another dictionary as an argument.Then it updates the dictionary
dict1.update(dict2)
print(dict1)

