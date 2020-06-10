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
