#Initializing a Tuple
tup_A = (3, 7, 4, 2)
#Access the first item of a tuple at index 0
print(tup_A[0])
#Print last item in the tuple
print(tup_A[-1])
#First index is inclusive (before the :) and last (after :) is not.
print(tup_A[0:2])
#Everything up to but not including index 3
print(tup_A[:3])
#Initialize tuple Tup1
Tup1 = ('Python', 'SQL')
#Initialize another tuple Tup2
Tup2 = ('R',)
#Create new tuple based on addition of tuples Tup1 and Tup2
newTuple = Tup1 + Tup2;
print(newTuple)
#Initialize a new tuple
tup_Animals = ('lama', 'sheep', 'lama', 48)
#The index method returns the first index at which a value occurs
print(tup_Animals.index('lama'))
#The count method returns the number of times a value occurs in a tuple
print(tup_Animals.count('lama'))
#Iterate through a tuple
for item in ('lama', 'sheep', 'lama', 48):
    print(item)
