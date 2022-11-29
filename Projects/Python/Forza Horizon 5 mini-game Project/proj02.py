#############################################################################
#  Project 2
#
# Print Welcome message and showing the user the information that \
# must be inputed if they choose to continue
#
# while loop is used to allow the user to play as long as possible
# prompting the user to continue playing the game or not.
# If user chooses option A, prompt user for classification code, days vehicle was rented, and odometer readings at start and the end.
# if user gives invalid value for classification code, then the program \ 
# will repeatedly prompt the user until a valid one is entered.
# Program prints the user's input then shows miles driven and amount due \
# based on the inputs.
# The game will keep looping itself until the user chooses option B \
# when given the choice to continue or not.
# When user chooses option B, a closing message is presented and game ends.
#############################################################################

import math

print("")
print("Welcome to Horizons car rentals. \n")
print("At the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BD, D, W) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")
print("")


while 1 > 0: #while loop to run program until user chooses option B
    PROMPT = input("Would you like to continue (A/B)? \n")
    if PROMPT == "B":
        print("Thank you for your loyalty.")
        break
    if PROMPT == "A":
        customer_code = input("\nCustomer code (BD, D, W): \n")
        if customer_code == "BD":
            
            _days_ = int(input("\nNumber of days: "))
            odo_start = int(input("\nOdometer reading at the start: "))
            odo_end = int(input("\nOdometer reading at the end:   "))
            print("")
            print("\nCustomer summary:")
            print("\tclassification code:", customer_code)
            print("\trental period (days):", _days_)
            print("\todometer reading at start:", odo_start)
            print("\todometer reading at end:  ", odo_end)
            if odo_end < 10: 
                odo_end = odo_end + 1000000
# This if-statement was used to battle the issue where user input showed \ 
# 000005 -999997 = 99999.2 to make code realistic           
            print("\tnumber of miles driven: ", abs(odo_start - odo_end) / 10)
            amount_due = 40*_days_ + 0.025*abs(odo_start - odo_end)
            amount_due = float(amount_due)
# The above 2 lines of code are equations for amount due if classification \ 
#code is BD
            print("\tamount due: $", amount_due / 1)
            print("")
            continue
        elif customer_code == "D":
            
            _days_ = int(input("\nNumber of days: "))
            odo_start = int(input("\nOdometer reading at the start: "))
            odo_end = int(input("\nOdometer reading at the end:   "))
            print("")
            print("\nCustomer summary:")
            print("\tclassification code:", customer_code)
            print("\trental period (days):", _days_)
            print("\todometer reading at start:", odo_start)
            print("\todometer reading at end:  ", odo_end)
            
            print("\tnumber of miles driven: ", abs(odo_start - odo_end) / 10)
            mile_per_day = (abs(odo_start - odo_end) / 10) / _days_
#mile_per_day is a variable I created to calculate average miles driven by \
# user per day
            amount_due_2 = 60 * (_days_)
            amount_due_3 = 60*(_days_) + (mile_per_day - 100)
            amount_due_2 = float(amount_due_2)
            amount_due_3 = float(amount_due_3)
# The above 4 lines of code are equations for amount due if classification \ 
#code is D with "amount_due_2" being base charge and amount_due_3 being \ 
# base charge and mileage charge, which are then converted to floats to \
# get values with decimal points. 
            if mile_per_day == 122.5:
                amount_due_3 = 60*(_days_) + 2*(mile_per_day - 100)
# the above if-statement was used to calculate amount due if average miles \
# per day was equal to 122.5
            if mile_per_day <= 100:
                print("\tamount due: $", amount_due_2)
                print("")
# the above if-statement was used to calculate amount due if average miles \
# per day was less thab 100  
            if mile_per_day > 100:
                print("\tamount due: $", amount_due_3)
                print("")
# the above if-statement was used to calculate amount due if average miles \
# per day was less thab 100  
            continue
        elif customer_code == "W":
            
            _days_ = int(input("\nNumber of days: "))
            odo_start = int(input("\nOdometer reading at the start: "))
            odo_end = int(input("\nOdometer reading at the end:   "))
            print("")
            print("\nCustomer summary:")
            print("\tclassification code:", customer_code)
            print("\trental period (days):", _days_)
            print("\todometer reading at start:", odo_start)
            print("\todometer reading at end:  ", odo_end)
            
            print("\tnumber of miles driven: ", abs(odo_start - odo_end) / 10)
            average_miles = (abs(odo_start - odo_end) / 10) / (math.ceil(_days_) / 7)
#average_miles is a variable I created to calculate average miles driven by \
# user per week  
            amount_due_4 = 190 * math.ceil(_days_ / 7)#for 900 miles and less
            amount_due_5 = 290 * math.ceil(_days_ / 7)# 900 - 1500 miles
            amount_due_6 = 202.5 * math.ceil(_days_ / 7) + 0.25*((abs(odo_start - odo_end) / 10) - 1500) #for miles > 1500
            amount_due_4 = float(amount_due_4)
            amount_due_5 = float(amount_due_5)
            amount_due_6 = float(amount_due_6)
# The above 6 lines of code are equations for amount due if classification \ 
#code is W with "amount_due_4" being base charge and is used if the \ 
#average amount of miles that user rode per week is less than 900 and \ 
#amount_due_5 being base charge and mileage charge if the average miles \ 
#per week that user drove is between 900 - 1500 miles, while \
# amount_due_6 is base charge and mileage charge if the average miles \ 
#per week that user drove is more than 1500 miles. All of this is shown \
# below as well.  
            
            if average_miles <= 900:
                print("\tamount due: $", amount_due_4)
                print("")
            elif 900 < average_miles <= 1500:
                print("\tamount due: $", amount_due_5)
                print("")
            else:
                print("\tamount due: $", amount_due_6)
                print("")
            continue
        else:
            print("\n\t*** Invalid customer code. Try again. ***")
            customer_code = input("\nCustomer code (BD, D, W): \n")
            if customer_code != "B" or customer_code != "D" or customer_code != "W":
                print("\n\t*** Invalid customer code. Try again. ***")
                customer_code = input("\nCustomer code (BD, D, W): \n")
# The above 6 lines of code show the if-statement if user input to \
#code is not "D", "BD" , or "W" and how it keeps repeating until user inputs
# either of these stings. 
        if customer_code == "BD":
            
            _days_ = int(input("\nNumber of days: "))
            odo_start = int(input("\nOdometer reading at the start: "))
            odo_end = int(input("\nOdometer reading at the end:   "))
            print("")
            print("\nCustomer summary:")
            print("\tclassification code:", customer_code)
            print("\trental period (days):", _days_)
            print("\todometer reading at start:", odo_start)
            print("\todometer reading at end:  ", odo_end)
            if odo_end < 10: #This if-statement was used to battle the \
# issue where user input showed 000005 -999997 to make code \ 
#realistic           
                odo_end = odo_end + 1000000
            
            print("\tnumber of miles driven: ", abs(odo_start - odo_end) / 10)
            amount_due = 40*_days_ + 0.025*abs(odo_start - odo_end)
            amount_due = float(amount_due)
# The above 2 lines of code are equations for amount due if classification \ 
#code is BD
            print("\tamount due: $", amount_due / 1)
            print("")
            continue
        elif customer_code == "D":
            
            _days_ = int(input("\nNumber of days: "))
            odo_start = int(input("\nOdometer reading at the start: "))
            odo_end = int(input("\nOdometer reading at the end:   "))
            print("")
            print("\nCustomer summary:")
            print("\tclassification code:", customer_code)
            print("\trental period (days):", _days_)
            print("\todometer reading at start:", odo_start)
            print("\todometer reading at end:  ", odo_end)
            
            print("\tnumber of miles driven: ", abs(odo_start - odo_end) / 10)
            mile_per_day = (abs(odo_start - odo_end) / 10) / _days_
#mile_per_day is a variable I created to calculate average miles driven by \
# user per day
            amount_due_2 = 60 * (_days_)
            amount_due_3 = 60*(_days_) + (mile_per_day - 100)
            amount_due_2 = float(amount_due_2)
            amount_due_3 = float(amount_due_3)
# The above 4 lines of code are equations for amount due if classification \ 
#code is D with "amount_due_2" being base charge and amount_due_3 being \ 
# base charge and mileage charge 
            if mile_per_day == 122.5:
                amount_due_3 = 60*(_days_) + 2*(mile_per_day - 100)
# the above if-statement was used to calculate amount due if average miles \
# per day was equal to 122.5
            if mile_per_day <= 100:
                print("\tamount due: $", amount_due_2)
                print("")
# the above if-statement was used to calculate amount due if average miles \
# per day was less thab 100  
            if mile_per_day > 100:
                print("\tamount due: $", amount_due_3)
                print("")
# the above if-statement was used to calculate amount due if average miles \
# per day was less thab 100  
            continue
        elif customer_code == "W":
            
            _days_ = int(input("\nNumber of days: "))
            odo_start = int(input("\nOdometer reading at the start: "))
            odo_end = int(input("\nOdometer reading at the end:   "))
            print("")
            print("\nCustomer summary:")
            print("\tclassification code:", customer_code)
            print("\trental period (days):", _days_)
            print("\todometer reading at start:", odo_start)
            print("\todometer reading at end:  ", odo_end)
            
            print("\tnumber of miles driven: ", abs(odo_start - odo_end) / 10)
            average_miles = (abs(odo_start - odo_end) / 10) / (math.ceil(_days_) / 7)
#average_miles is a variable I created to calculate average miles driven by \
# user per week  
            amount_due_4 = 190 * math.ceil(_days_ / 7)#for 900 miles and less
            amount_due_5 = 290 * math.ceil(_days_ / 7)# 900 - 1500 miles
            amount_due_6 = 202.5 * math.ceil(_days_ / 7) + 0.25*((abs(odo_start - odo_end) / 10) - 1500) #for miles > 1500
            amount_due_4 = float(amount_due_4)
            amount_due_5 = float(amount_due_5)
            amount_due_6 = float(amount_due_6)
# The above 6 lines of code are equations for amount due if classification \ 
#code is W with "amount_due_4" being base charge and is used if the \ 
#average amount of miles that user rode per week is less than 900 and \ 
#amount_due_5 being base charge and mileage charge if the average miles \ 
#per week that user drove is between 900 - 1500 miles, while \
# amount_due_6 is base charge and mileage charge if the average miles \ 
#per week that user drove is more than 1500 miles. All of this is shown \
# below as well.  
            
            if average_miles <= 900:
                print("\tamount due: $", amount_due_4)
                print("")
            elif 900 < average_miles <= 1500:
                print("\tamount due: $", amount_due_5)
                print("")
            else:
                print("\tamount due: $", amount_due_6)
                print("")
            continue
        else:
            print("\n\t*** Invalid customer code. Try again. ***")
            customer_code = input("\nCustomer code (BD, D, W): \n")
            if customer_code != "B" or customer_code != "D" or customer_code != "W":
                print("\n\t*** Invalid customer code. Try again. ***")
                customer_code = input("\nCustomer code (BD, D, W): \n")
# The above 7 lines of code show the if-statement if user input to \
#code is not "D", "BD" , or "W" and how it keeps repeating until user \ 
# inputs either of these stings.