#Initialize dictionary
myDict = {3:3, 1:1, 4:4}
print(myDict)
#The keys() method returns a list of keys in a python dictionary
print(myDict.keys())
#The values() method returns a list of values in the dictionry.
print(myDict.values())
#The items() method returns a list of key-value pairs.
print(myDict.items())
#The copy() method creates a shallow copy of the python dictionary.
newDict = myDict.copy()
print(newdict)
#The pop() method is used to remove and display an item from the dictionary
print(newDict.pop(4))
#Reassigning python dictionary newDict
newDict = {3:3, 1:1, 4:4, 7:7, 9:9}
#The popitem() method is used to pop pair.
print(newDict.popitem())
#The fromkeys() method creates a new Python dictionary from an existing one.
print(newDict.fromkeys({1, 2, 3, 4, 7}, 0))
#Initialize dictionaries Dict1 and Dict2
Dict1={1:1, 2:2}
Dict2={2:2, 3:3}
#The update() method takes another dictionary as an argument.Then it updates the dictionary
Dict1.update(Dict2)
print(Dict1)

