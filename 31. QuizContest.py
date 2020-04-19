#Build an interactive application which should simulate a Quiz contest.
 #The following questions might be asked as input from user:

def playQuiz(dicision):
    if dicision == 'y':
        Quiz()
    else:
        print("Thanks for playing Quiz, visit again!!!\n")
        
def func(optedlevel,optedTypes):
    numberOfAtempt=5
    
    def calculation(operation):
        return operation(optedlevel)
    
    while numberOfAtempt >0:
        result = calculation(optedTypes)
        userAnswer = int(input("Enter your answer "))
        if userAnswer == result:
            print("\nCorrect Answer\n")          
            break
        else:
            numberOfAtempt = numberOfAtempt-1
            print("Worng answer\nRemaining attempts are {}\n".format(numberOfAtempt))
    else:
        print("Wrong answer, bad luck!!!\n")

def generateRandom(a,b):
    import random
    return random.randint(a,b)

def multiplication(optedlevel):
    if optedlevel =='easy':
        dificultRange = 20
        number1 = generateRandom(1,dificultRange)
        number2 = generateRandom(1,15)
    elif optedlevel =='intermediate':
        dificultRange = 500
        number1 = generateRandom(100,dificultRange)
        number2 = generateRandom(1,35)
    else:
        dificultRange = 5000
        number1 = generateRandom(500,dificultRange)
        number2 = generateRandom(1,99)
    print("Product of {} and {} is \n".format(number1,number2))
    return number1*number2

def addition(optedlevel):
    
    if optedlevel =='easy':
        dificultRange = 50
        number1 = generateRandom(10,dificultRange)
        number2 = generateRandom(1,dificultRange)
    elif optedlevel =='intermediate':
        dificultRange = 500
        number1 = generateRandom(100,dificultRange)
        number2 = generateRandom(1,dificultRange)
    else:
        dificultRange = 5000
        number1 = generateRandom(500,dificultRange)
        number2 = generateRandom(1,dificultRange)
    print("Addition of {} and {} is \n".format(number1,number2))
    return number1+number2

def subtraction(optedlevel):
    
    if optedlevel =='easy':
        dificultRange = 20
        number1 = generateRandom(10,dificultRange)
        number2 = generateRandom(1,dificultRange)
    elif optedlevel =='intermediate':
        dificultRange = 500
        number1 = generateRandom(100,dificultRange)
        number2 = generateRandom(1,dificultRange)
    else:
        dificultRange = 5000
        number1 = generateRandom(500,dificultRange)
        number2 = generateRandom(1,dificultRange)
    print("differnce of {} and {} is \n".format(number2,number1))
    return number2-number1

def division(optedlevel):
    
    if optedlevel =='easy':
        dificultRange = 50
        number1 = generateRandom(10,dificultRange)
        number2 = generateRandom(1,10)
    elif optedlevel =='intermediate':
        dificultRange = 500
        number1 = generateRandom(100,dificultRange)
        number2 = generateRandom(1,30)
    else:
        dificultRange = 5000
        number1 = generateRandom(500,dificultRange)
        number2 = generateRandom(1,99)
    print("What's {} divided by {}? \n".format(number1,number2))
    return number1//number2
    
#.............. main func.....................

def Quiz():
#1.Choose level (easy, intermediate, and hard):
 # three modes of difficulty and user should input one of these choices
    modes = {1:'easy',2:'intermediate',3:'hard'}
    print("Welcome to Airthmatic Quiz!!!")
    while(True):
        level = int(input("Choose the level for below modes \n 1.easy\n 2.intermediate\n 3.hard\n"))
    
        if int(level) not in modes.keys():
            print("Please enter 1,2 and 3 for valid input\n")
        else:
            optedlevel = modes[level]
            print("You choosed to play the game {}".format(optedlevel))
            break
    
        
#2.Please give us the number of question you want to attempt:
 #No of questions thrown should be the number entered through this prompt
        
    while(True):
        NoOfQuestions = int(input("select the number of questions to attempt the Quiz\n"))
        if (5 < NoOfQuestions) and (NoOfQuestions < 20):
             print("you selected {} questions to answer".format(NoOfQuestions))
             break
        else:
            print("Please enter number of questions between 5 and 20\n")
            
        
#3.Specify the questiontype (multiplication:M, addition:A, subtraction:S, division:D):
 #One of these operations to be performed

    types = {'M':multiplication, 'A':addition, 'S':subtraction, 'D':division}
    while(True):
        selectTypes = input("Select the below type {}\n".format(types.values()))

        if selectTypes.upper() not in types.keys():
            print("Please enter 'M','A', 'S' and 'D' for valid input\n")
        else:
            optedTypes = types[selectTypes.upper()]
            print("you choose {}\n".format(optedTypes.values()))
            break
    print("let's begin\n")   
    while(NoOfQuestions>=1):
        func(optedlevel,optedTypes)
        
        print("\nnext question\n")
        NoOfQuestions = NoOfQuestions-1
        print("remaining questions {}\n".format(NoOfQuestions))
    
    decision = input("Thanks for playing the game.\n if you want to continue press Y else N\n")
    playQuiz(decision.lower())
    
Quiz()
                  
