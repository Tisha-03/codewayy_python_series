#Initializing my_set
mySet={1, 2, 3, 4, 5, 6}
print(mySet)
#Discard or remove an element
mySet.discard(4)
print(mySet)
mySet.remove(6)
print(mySet)
#Initialize setA
setA=set("HelloWorld")
print(setA)#displays set of unique elements
#Pop an element
print(setA.pop())
#Clear setA
setA.clear()
print(setA)

#Python set Operations

#Initialize setB and setC
setB={1, 2, 3, 4}
setC={4, 5, 6, 7}
#Union Method
print(setB.union(setC))
print(setC.union(setB))
#Intersection method
print(setB & setC)
#Set Difference method
print(setB - setC)
#Set Symmetric Difference method
print(setB ^ setC)
