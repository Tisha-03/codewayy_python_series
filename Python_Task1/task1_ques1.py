#Operations on integer values
a=int(input("Enter integer value "))
b=int(input("Enter integer value "))
print("Multiplication of two integers is ",a*b)
print("Division of two integers is ",a/b)
print("Addition of two integers is ",a+b)
print("Subtraction of two integers is ",a-b)
print("Exponent of a to b is ",a**b)
print("Floor Division of two integers is ",a//b)
#Operation on float values
x=float(input("Enter one Float value "))
y=float(input("Enter another float value "))
print(x*y)
print(x/y)
print(x+y)
print(x-y)
print(x**y)
print(x//y)
#Displaying name using string concatenation
first_name=input("Enter your First name ")
last_name=input("Enter your Last name ")
print(first_name + " "+last_name)
#Displaying College name with address using string concatenation
college_name=input("Enter College Name ")
address=input("Enter address of college ")
print(college_name + " " +address)
#Initialising marks of 5 different subjects
Math_marks=int(input("Enter your Maths marks "))
Eng_marks=int(input("Enter your English marks "))
Science_marks=int(input("Enter your Science marks "))
Hindi_marks=int(input("Enter your Hindi marks "))
Computer_marks=int(input("Enter your Computer marks "))
total_marks=Math_marks+Eng_marks+Science_marks+Hindi_marks+Computer_marks
per=total_marks/5
print("Total marks are ",total_marks)
print("Percentage is ",per)



