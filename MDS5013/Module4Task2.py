import math
#Define and call the function to calculate LCM of a number 

def find_lcm(x,y):
    
    #choose greater number
    greater = x 
    if y > greater:
        greater = y

    while(True):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
        break
    
    greater += 1
    
    return lcm

num_1 = int(input("Enter numb_1: "))
num_2 = int(input("Enter numb_2: "))
#print("The LCM is ",find_lcm(num_1,num_2))
print("The LCM is ", find_lcm(num_1,num_2))