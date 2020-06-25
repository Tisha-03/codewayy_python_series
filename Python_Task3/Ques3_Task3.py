#Printing numbers from 1 to 10 except 3 and 7 using for loop
for x in range(1,11):
    if(x == 3 or x == 7):
        continue
    print(x,end=' ')
print("\n")
#Printing numbers from 1 to 10 except 3 and 7 using while loop
number=1
while(number!=11):
    if(number == 3 or number == 7):
        number+=1
    else:
        print(number)
        number+=1

