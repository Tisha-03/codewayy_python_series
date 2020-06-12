#Initializing my_set
my_set={1, 2, 3, 4, 5, 6}
print(my_set)
#Discard or remove an element
my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)
#Initialize set A
A=set("HelloWorld")
print(A)#displays set of unique elements
#Pop an element
print(A.pop())
#Clear set A
A.clear()
print(A)

#Python set Operations

#Initialize set B and C
B={1, 2, 3, 4}
C={4, 5, 6, 7}
#Union Method
print(B.union(C))
print(C.union(B))
#Intersection method
print(B & C)
#Set Difference method
print(B - C)
#Set Symmetric Difference method
print(B ^ C)
