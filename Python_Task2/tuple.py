#Initializing a Tuple
z = (3, 7, 4, 2)
#Access the first item of a tuple at index 0
print(z[0])
#Print last item in the tuple
print(z[-1])
#First index is inclusive (before the :) and last (after :) is not.
print(z[0:2])
#Everything up to but not including index 3
print(z[:3])
#Initialize tuple1
tup1 = ('Python', 'SQL')
#Initialize another tuple2
tup2 = ('R',)
#Create new tuple based on addition of tuples tup1 and tup2
new_tuple = tup1 + tup2;
print(new_tuple)
#Initialize a new tuple
animals = ('lama', 'sheep', 'lama', 48)
#The index method returns the first index at which a value occurs
print(animals.index('lama'))
#The count method returns the number of times a value occurs in a tuple
print(animals.count('lama'))
#Iterate through a tuple
for item in ('lama', 'sheep', 'lama', 48):
    print(item)
