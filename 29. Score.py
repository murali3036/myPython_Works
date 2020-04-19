#Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range print an error.
#If the score is between 0.0 and 1.0, print a grade using the following table:

grades = {0.9:'A',0.8:'B',0.7:'C',0.6:'D',0.5:'Fail',0.4:'Fail',0.3:'Fail',0.2:'Fail',0.1:'Fail'}
import math
while(True):
    score = float(input("Please enter your grade "))
    if score > 0.0 and score < 1.0:
        x = math.floor(score*10)/10
        print(grades[x])
        
    else:
        print("Bad score")
