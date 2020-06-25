#Function to return full name
def displayName():
    Name=input("Enter your full name")
    print("Your Name is",Name)
#function to return total marks
def displayTotalMarks():
    Eng_Marks=int(input("Enter your Eng_Marks "))
    Maths_Marks=int(input("Enter your Maths marks "))
    Science_Marks=int(input("Enter your Science marks "))
    Arts_Marks=int(input("Enter your arts marks "))
    Hindi_Marks=int(input("Enter your Hindi marks "))
    global totalMarks
    totalMarks=Eng_Marks+Maths_Marks+Science_Marks+ Arts_Marks+Hindi_Marks
    print("Total marks are ",totalMarks)
#function to return percentage
def displayPercentage(totalMarks):
    global calPercentage
    calPercentage=(totalMarks/5)
    print("Your Percentage is",calPercentage)
#function to return grade
def displayGrade(calPercentage):
    if(calPercentage>=95):
        print('Your Grade is A')
    if(calPercentage>=85 and calPercentage<=95):
        print('Your Grade is B')
    if(calPercentage>=75 and calPercentage<=85):
        print('Your Grade is C')
    if(calPercentage>=65 and calPercentage<=75):
        print('Your Grade is D')
    else:
        print("Failed")
#function to return all other functions
def displayAllDetails():
    displayName()
    displayTotalMarks()
    displayPercentage(totalMarks)
    displayGrade(calPercentage)
#Calling that function 
displayAllDetails()
    
    


    
    
