#Defining list
List=['Hindi' , 'Science' , 'Computer' , 'Psychology' , 2000 , 2122]
print(List)
#Adds List Element as value of List.
List.append(2909) 
print(List)
#Insert at index 2 value 128
List.insert(2, 128)
print(List)
#Defining List 1 and List 2
List1=[1, 2, 3]
List2=[2, 3, 4, 5]
#Add List2 to List1
List1.extend(List2)
print(List1)
#Add List1 to List2
List2.extend(List1)
print(List2)
#Defining new List3
List3=[1, 2, 3, 4, 5]
#Calculates sum of all the elements of List3
print(sum(List3))
#Defining List4
List4=[1, 2, 3, 4, 2, 3, 4, 1, 2, 3]
#Calculates total occurence of given element of List4
print(List4.count(3))
#Calculates total length of List4
print(len(List4))
#Calculates minimum of all the elements of list4
print(min(List4))
#Calculates maximum of all the elements of list4
print(max(List4))
