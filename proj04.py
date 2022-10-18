#############################################################################
# Project 4
# In this project, the purpose was to create 6 functions which are a \
# factorial function, e function, pi function, sinh function, menu function \
# and mainfunction. A 7th function was created called "factorialz()" \
# to be able to interact with the user which the function "factorial()" \
# could not do.
# Firstly, the project displays the list of options that the user can select.
# These options are labelled, "F", "E", "P", "S", "M", "X". If the user \
# inputs either the lowercase or uppercase version of letter; either will \
# be accepted. "F" will preform the factorial calculations and will run the \
# "factorialz()" function for a user input. "E" will output the calculated \
# value for "e" using a mathematical formula, and will also present the \
# mathematical value for "e" as well as the absolute value for the \
# difference between both values. "P" will output the calculated \
# value for "pi" using a mathematical formula, and will also present the \
# mathematical value for "pi" as well as the absolute value for the \
# difference between both values. "S" will accept a user input as a str \
# and if the string can be converted to a number, then the sinh calculation \
# will be preformed using an equation, and also the mathematic value for \
# sinh will be outputed as well as the difference between both values. If \
# the user selects "M", the menu of the options that the user can select from
# are shown. If the user selects "X", then the game presents a closing \
# message and ends. A while loop is used to keep prompting the user to \
# select an option to keep continue playing the game or to exit.Also in the \
# case where the user inputs an invalid character when the menu is shown \
# The program will tell the user that the option inputted is invalid, then \
# it shows the menu and allows the user to input a value again.
#############################################################################

import math 
import sys # imported to use sys.exit() to abruptly end the program when code is not under a while\
#loop
def factorial(N):
    """
    Function accepts user input as a str, and then will try to convert the \
    input to an integer value. This is done through the use of for loop to \
    enumereate each character in the user's input. If there is a character \
    in the user's input that is a lowercase letter (The function only\
    accounted for lowercase letters) then the function would return None. \
    Otherwise the function will convert the input to an integer and then \
    will check if the input is positive or negative. If the value is \
    negative, then the function returns None. If the value is positive, a \ 
    calculation is done to calculate the factorial of the number using a \
    for loop and range function then it will return Factorial (that is the \
    name of the variable where the value of the int is stored.
    """
    factorial = 1 #this was done to indicate that 0! = 1
    strings = "abcdefghijklmnopqrstuvwxyz"
    empty = ""
    for i,ch in enumerate(N):
        if ch in strings:
            return None
        elif empty == "":
            N = int(N)
            if N < 0:
                return None
                break
            if N > 0:
                for i in range(1,N + 1):
                    factorial = factorial*i
            return factorial 


def factorialz():
    """
    Function accepts user input as a str, and then will try to convert the \
    input to an integer value. This is done through the use of for loop to \
    enumereate each character in the user's input. If there is a character \
    in the user's input that is a lowercase letter (The function only \
    accounted for lowercase letters) then the function would print \
    "Invalid N". Otherwise the function will convert the input to an \
    integer and then will \ check if the input is positive or negative. \
    If the value is negative, then \ the function would print "Invalid N".\
    If the value is positive, a calculation is done to calculate the \
    factorial of the number using a for loop and range function then it \
    will print Factorial (that is the name of the variable where the \
    value of the int is stored.
    """
    N = input("Input non-negative integer N: ")
    factorial = 1  #this was done to indicate that 0! = 1
    strings = "abcdefghijklmnopqrstuvwxyz-"
    empty = ""

    if N[0:1] in strings and N[0:1] != "" and empty == "": # this was done \
    # to make the function print "Invalid N." if the first character of the \
    # input was in the variable "strings".
        print("")
        print("Invalid N.")
        print("")
    elif N[1:2] in strings and N[1:2] != "" and empty == "": # this was done\
    # to make the function print "Invalid N." if the second character of the\
    # input was in the variable "strings".
        print("")
        print("Invalid N.")
        print("")
    
    else: # this checks for letters for all characters after the second character.
    
        for i, ch in enumerate(N):
            if ch in strings:
                empty += ch
            
    
        
            if empty == "": #if empty == "" then N only includes characters \
            # that can be converted to integer values.
                N = int(N)
                if N < 0:
                    break
                    
                elif N > 0: # This elif statement calculates the factorial \
                # for user input using a for loop.
                    for i in range(1,N + 1):
                        factorial = factorial*i
                    print("")
                    print("Calculated:", factorial)
                    print("Math:", math.factorial(N))
                    print("Diff:", abs(factorial - math.factorial(N)))
                    print("")
            elif empty != "":
                print("Invalid N.")
            

def e():
    """
    This function takes no parameters and returns an approximate value of e. An equation is used \
    that utilizes "summation" and keeps adding terms up until the term that is reached is smaller \
    than EPSILON (a variable created to represent the value 0.0000001) which is an arbitrary term.
    The answer is then rounded to 10 decimal places.
    """
    x = 0 
    EPSILON = 0.0000001
    while math.factorial(x) < 1 / EPSILON:
        x += 1 # this was done to comply with mathematical equation provided.
        n = 10 # at the nth term (which is equal to 10), the value of the term to be added, so \
        # the 10th term will be equal or less than EPSILON, so terms keep adding on until the \
        # n + 1 term.
        s = 0.0
    for i in range(0, n + 1):
        s += 1.0 / math.factorial(i)
    s = round(s, 10) 
    return s

def pi():
    """
    This function takes no parameters and returns an approximate value of pi. An equation is used \
    that utilizes "summation" and keeps adding terms up until the term that is reached is smaller \
    than EPSILON (a variable created to represent the value 0.0000001) which is an arbitrary term.\
    The answer is them rounded to 10 decimal places
    """
    denominator = 1
    EPSILON = 0.0000001 
    
    s = 0 #this variable indicates starting value
    n = 0 # n is the starting value for the summation series
    while ((1) / (2*n + 1)) >= EPSILON:
        n += 1
        continue
    for i in range(n): # the whole point of this for loop is to check if -1 is raised to a positive\
    # or negative power. if power is even, then the -1 will become 1, otherwise will stay odd.
        if i % 2 == 0:
            s += 4 / denominator
        else:
            s -= 4/ denominator
        denominator += 2
         
    s = round(s, 10)
    return s
 

def sinh(x):
    """
    This function takes str as a parameter and returns an approximate value for the sinh() \ 
    value that based on what is the input that the user provided. An equation is used \
    that utilizes "summation" and keeps adding terms up until the term that is reached is smaller \
    than EPSILON (a variable created to represent the value 0.0000001) which is an arbitrary term.\
    The answer is them rounded to 10 decimal places.
    """
    EPSILON = 0.0000001
    n = 1 #variable in equation provided in project description.
    phi = 0 # this term will be the one that will be returend to the user and its value will keep \
    # increacing until value of next term is less than EPSILON.
    numbers = "0123456789.-" # these are the characters that can be used to convert the input to \
    # a floating point value so that the function can actuallly be called.
    letters = "abcdefghijklmnopqrstuvwxyz" # these are the characters that can't be converted to \
    # float, so if they are inputed, the function returns None. 
    empty = "" # This variable will be used to input valid characters that can be converted to \
    # floating point values so that the function can run without any errors.

    d = 0 # This variable was created to solve an issue where if the user input contains a \
    # character from "letters" and a character from "numbers" the code would crash; ie: "2a".
    for index, ch in enumerate(x): #checks each character in input to see if character is valid \
    # or not.
        if ch in numbers:
            empty += ch
            d +=2
        if ch in letters:
            d -= 1
    if d < 1: #This value of d indicates that there mist be a character in letters that was \
    # inputted by the user, so "sys.exit()" was used to end the function.
        sys.exit()
    empty = float(empty)
    if empty < 0: # This applies only if the input of the user is less than zero.
        empty = abs(empty)
        for i in range(0, 100):
            equation = empty**n / math.factorial(n)
            if equation < EPSILON: 
                return round(-1 * phi, 10)
                break
            else: # keeps adding terms until term is smaller than EPSILON.
                phi += equation
                n +=2
    elif empty > 0: # This applies only if the input of the user is more than zero.
        for i in range(0, 100):
            equation = empty**n / math.factorial(n)
            if equation < EPSILON:
                return round(phi, 10)
                break
            else:
                phi += equation
                n +=2




def menu():

    """
    When this function is called, it will print out the menu of options that the user can \
    select from. It has no parameter and does not return anything.
    """
    print("")
    print("Options below:")
    print("    ‘F’: Factorial of N.")
    print("    ‘E’: Approximate value of e.")
    print("    ‘P’: Approximate value of Pi.")
    print("    ‘S’: Approximate value of the sinh of X.")
    print("    ‘M’: Display the menu of options.")
    print("    ‘X’: Exit.")
    print("")
    print("")


def main():
    """
    This function is the one that will be run and will interact with the user. Within it, only \
    the "factorialz()" function is used, as the other ones do not interact with the user. Code \
    has been written that is simmilar to the functions created above, except they differ in that \
    they interact with the user and print values rather than returning them. The "menu()" function\
    is also used within this function.
    """
    count = 0 
    EPSILON = 0.0000001 
    while True:
        if count == 0: # This was done purposefully so that the menu is only shown once in the \
        #begining and also when the user selects the prompt to view the menuu.
            menu()
            count +=1
        elif count != 0: #this was done to always prompt the user to provide an option since this \
        # is nested under a while loop.
            x = input("Choose an option: ")
            
            if x == "F" or x == "f":
                print("")
                print("Factorial")
               
                factorialz() #calling function
                
                    

            elif x == "E" or x == "e":
            #This option prints an approximate value of e, mathematical value of e, and difference\
            #between both values.An equation is used that utilizes "summation" and keeps adding \
            #terms up until the term that is reached is smaller than EPSILON (a variable created to\ 
            #represent the value 0.0000001) which is an arbitrary term. The answer is then rounded\ 
            #to 10 decimal places.

                x = 0 
                EPSILON = 0.0000001
                while math.factorial(x) < 1 / EPSILON:
                    x += 1 # keeps adding terms, to follow the mathematical formula to approximate\
                    # the value of e

                    n = 10 # at the nth term (which is equal to 10), the value of the term to be \
                    # added so the 10th term will be equal or less than EPSILON, so terms keep \
                    # adding on until the  n + 1 term.

                    s = 0.0 #variable "s" is used to indicate starting value, which is zero, and \
                    # the value will keep increacing up until the term reached is less than or \
                    # equal to EPSILON.
                for i in range(0, n + 1):
                    s += 1.0 / math.factorial(i)
                s = round(s, 10)
                print("")
                print("e")
                print("Calculated:",s)
                print("Math:", round(math.e, 10))
                print("Diff: {:.10f}".format(abs(s - math.e)))
                print("")
            elif x == "p" or x == "P":
                denominator = 1
                
                s = 0 #variable "s" is used to indicate starting value, which is zero, and \
                    # the value will keep increacing up until the term reached is less than or \
                    # equal to EPSILON.

                n = 0 # starts at 0 and keeps increacing. This variable is used in the denominator \
                # of the mathematical equation that is used to calculate pi.
                while ((1) / (2*n + 1)) >= EPSILON:
                    n += 1
                    continue
                for i in range(n):
                    if i % 2 == 0: # this statement is used in case -1 is raised to a positive \
                    # power in the mathematical equation used to calculate pi.
                        s += 4 / denominator
                    else: # this statement is used in case -1 is raised to a negative power in the \
                    # mathematical equation used to calculate pi.
                        s -= 4/ denominator
                    denominator += 2
                    
                print("")
                print("pi")
                print("Calculated:", round(s, 10))
                print("Math:", round(math.pi, 10))
                print("Diff: {:.10f}".format(abs(s - math.pi)))
                print("")
            
            elif x == "s" or x == "S":
                print("")
                print("sinh")
                EPSILON = 0.0000001
                n = 1 #The variable n's value will keep changing by +2, it is part of the \
                # mathematical formula used to calculate the approximate value of 
                phi = 0 # this variable will start at zero and its value will keep on increacing \
                # until the value of the next term to be added is less than or equal to EPSILON.
                x = input("X in radians: ")
                numbers = "0123456789.-" # these are the characters that can be used to convert the\
                #input to a floating point value so that the function can actuallly be called.
                letters = "abcdefghijklmnopqrstuvwxyz" # these are the characters that can't be \ 
                #converted to float, so if they are inputed, the function returns None. 
                empty = ""
                # "empty" will be used to input valid characters that can be converted to \ 
                # floating point values so that the function can run without any errors.
                
                d = 0 # variable "d" will act as a counter that acts in a unique way, in that if \
                # the value is equal to 1, it recognizes that the inputed value is invalid to have \
                # a sinh() value, whereas if it is more than 1then it is possible.
                for index, ch in enumerate(x): #checks each character in user input.
                    if ch in numbers:
                        empty += ch
                        d +=2
                    if ch in letters:
                        d -= 1
                if d > 1: #recognizes that input can be converted to a float, so continues with the \
                # code.
                    empty = float(empty) 
                    for i in range(0, 100):
                        equation = empty**n / math.factorial(n) # mathematical formula to estimate \
                        # value of sinh(x).
                        if equation < EPSILON: # to stop adding terms if the term is less than\
                        # EPSILON
                            print("")
                            uu = phi
                            yy = math.sinh(empty)
                            xj = abs(round(uu, 10) - round(yy, 10))
                            xj = "{:.10f}". format(xj)
                            # The above 4 variables were used to make the code look more presentable\
                            # and less condensed, to allow for easier reading of the code. They mean\
                            # nothing, their name is irrelevant and their only purpose is asthetics.
                            print("Calculated:", round(phi, 10))
                            print("Math:", round(math.sinh(empty), 10))
                            print("Diff:", xj )  
                            print("")
                            break
                        else: # This was used to continue with the summation and change the power \
                        # that is raised in the equation.
                            phi += equation
                            n +=2
                if d == 1: # program detects that user input is invalid
                    print("")
                    print("Invalid X.")
                    print("")
                if x in letters: # program detects that user input is invalid
                    print("")
                    print("Invalid X.")
                    
                
            elif x == "m" or x == "M":
                menu() # calls menu
            elif x == "x" or x == "X":
                print("\nThank you for playing.")
                break
            
            else: # if user inputs an invalid character, this also calls menu() to show user list\
            # of options.
                print("\nInvalid option:", x.upper())
                menu() #function menu() is called
if __name__ == '__main__': # this line was used so that each function would be individually tested.
    main()