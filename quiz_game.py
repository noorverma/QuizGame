print ("Welcome to my Quiz")

playing = input("Do you want to play? ")


if playing.lower() != "yes": #not equal to operator, lower converts the answer to lower cases
    quit() #make sure to indent indentation is needed to make the code work properly
   
print ("Okay let's play :)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit": #equality operator we use if else here 
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphic processing unit": #equality operator we use if else here 
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("What does OOP stand for? ")
if answer.lower() == "object oriented programming": #equality operator we use if else here 
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("What does VM stands for? ")
if answer.lower() == "virtual machine": #equality operator we use if else here 
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("What does SQL stands for? ")
if answer.lower() == "structural query language": #equality operator we use if else here 
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

print ("You got " +str(score)+ "correct")
print ("You got " + str((score/5)*100)+ "correct" )