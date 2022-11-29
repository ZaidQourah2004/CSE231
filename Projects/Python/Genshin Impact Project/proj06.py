###############################################################################
# Project 6
# The objective of this program is open and read a csv file that shows data \
# from the video game GENSHIN. Then this program allows the user to select an \
# option from a character directory which contains information regarding, all \
# available regions and characters. Characters can be filterd through \
# a certain criteria or multiple different criterias. Different outputs are \
# displayed depending on user inputs, which also account for the user not \
# lisenting to instructions given in code (like entering a string when an int \
# should be inputted). This function (the one that interacts with the user is \
# "main()"), other functions were written as a part of this program and were \
# used and called inside main when needed.
###############################################################################

import csv # to read csv files
from operator import itemgetter # to sort items based on rarity

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    """
    Accepts user input to user input to open file \
    Keep prompting the user until a valid filename is entered. "file_pointer" \
    is returned which opens a valid file.
    """
    
    while True: # to keep looping incase invalid option is entered.
        PROMPT = input("Enter file name: ")
        try:
            fp = open(PROMPT, "r") 
            break # to stop loop since valid option is entered
            
        except FileNotFoundError: #try-except used to prevent code crashing
            print("\nError opening file. Please try again.")
            continue
            
            
        fp = open(PROMPT, "r") 
        return fp

    

def read_file(fp):
    """
    This function reads the file that was provided based on the user input \
    as to why the parameter "fp" was used, so this function reads fp and stores \
    data in a list. This function returns the appended list.
    """
    reader = csv.reader(fp)
    next(reader,None) #skips header line as it is irrelevant
    data = [] # empty data set and will be filled with info from file that is \
    # read
    for line in reader: # loops through each line in file
        Name = line[0]
        Element = line[2]
        Weapon = line[3]
        Rarity = int(line[1])
        Region = line[4]
        # above 4 lines organize data from the file to correctley add them to \
            # list.
        tup = (Name,Element,Weapon,Rarity,Region or None) 
        data.append(tup)
    fp.close()
    return data


def get_characters_by_criterion (list_of_tuples, criteria, value):
    """
    This function filters characters based on the criterion chosen and the \
    value chosen for that criteria. This function then extracts the data from \
    the file that matches the specific criteria and values chosen by user, so \
    that the filtered data can be added to an empty list. This function returns \
    appended list with filtered data.
    """
    data = []

    for tup in list_of_tuples:
        if criteria == 3: # converts value for rarity to an int value.
            try:
                tup[3] == int(tup[3])
                value = int(value)
                if tup[3] == value:
                    data.append(tup)
            except ValueError:
                continue
        elif criteria == 1:
            value = value.capitalize()
            if tup[1] == value:
                data.append(tup)
        elif criteria == 4:
            value = value.capitalize()
            if tup[4] == value:
                data.append(tup)
        elif criteria == 2:
            value = value.capitalize()
            if tup[2] == value:
                data.append(tup)
        # the three elif statment capitalize info from file, to make it more \
        # presentable when added to the empty dataset. Every item is added to \
        # the list but in a formatted way that is mutable.

    return data
          
        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    """
    This function filters characters based on 3 the values of criteria and \
    value chosen for chosen criteria. Function then extracts the data from \
    the file that matches the specific criteria and values chosen by user, so \
    that the filtered data can be added to an empty list. This function returns \
    appended list with filtered data.
    """
    data = []
    for item in master_list: #checks each tuple within the master list.
        element = element.capitalize()
        weapon = weapon.capitalize()
        if item[1] == element and item[2] == weapon and item[3] == rarity:
            #checks each item within the tuple in the list and adds it to the \
                # new list, to make the items mutable.
            data.append(item) # appends mutable item
        
    return data # returns data with all items mutable.

def get_region_list(master_list):
    """
    This function collects all available regions from the master list, it \
    checks each item in a list and then slices  item to find a specific item \
    within the item, and adds it to a new list (which is empty). If the sliced \
    item is empty (or None) or has already been appended to the list, then it \
    is not added. Data is sorted alphabetically then it is returned.
    """
    data = []
    for item in master_list:
        if item[4] == None: # skips over empty item or None or ""
            continue
        if item[4] not in data: # adds item if not already in data set, else \
            # item is ignored.
            data.append(item[4])
    data.sort() #sorts data in alphabetical order

    return data 
    pass

def sort_characters (list_of_tuples):
    """
    This function makes a copy of the data provided by the file, and stores it \
    in a list, then this function sorts the data in terms of the third element \
    (rarity) which has been converted to an integer value in decsending \
    order based on the value for rarity and the new data list is changed \
    accordingly, that new list is returned by the function.
    """
    data = []
    for tup in list_of_tuples:
        tup[3] == int(tup[3])
        data.append(tup)
    data.sort()
    new_data = sorted(data, key = itemgetter(3), reverse = True)
    return new_data
    pass

def display_characters (list_of_tuples):
    """
    This function does not return anything but it does display the information \
    in the csv files (or in any list) in a presentable way with headers shown \
        neatly as they are formatted and so are the rows for the data. If an \
        item is None, it is replaced with "N/A"
    """
    if list_of_tuples == "": #if list it empty

        print("Nothing to print. ")
    else:
        a = "Character"
        b = "Element"
        c = "Weapon"
        d = "Rarity"
        e = "Region"
        # above variable names are arbitrary and are used  to not exceed 80 \
        # character limit
        print("\n{:20s}{:10s}{:10s}{:<10s}{:25s}".format(a,b,c,d,e))

        for tup in list_of_tuples: # accounts for when the region of a certain \
            # list is not mentioned.
            tup = list(tup)
            if tup[4] == None:
                tup[4] = "N/A"
            print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(tup[0],tup[1],tup[2],tup[3],tup[4]))


def get_option():
    """
    This function does not return anything but it does display options\
    that the user can chhose from. This function keeps looping until user inputs\
    4, and if an invalid option is entered the function will keep looping until
    a valid option is entered.
    """
    while True: # keeps looping
        x = (input(MENU)) #variable name is arbitrary and used only to make code \
            # look nicer.
        try:
            x = int(x)            
            if  1<= x <= 4:
                return x
            else:
                print(INVALID_INPUT)
                pass
        except ValueError:
            print(INVALID_INPUT)
            x = -1
            if 1<= x <= 4:
                return x
            else:
                continue

def main():
    """
    The objective of this program is open and read a csv file that shows data \
    from the video game GENSHIN. Then this program allows the user to select an \
    option from a character directory which contains information regarding, all \
    available regions and characters. Characters can be filterd through \
    a certain criteria or multiple different criterias. Different outputs are \
    displayed depending on user inputs, which also account for the user not \
    lisenting to instructions given in code (like entering a string when an int \
    should be inputted). This function (the one that interacts with the user is \
    "main()"), other functions were written as a part of this program and were \
    used and called inside main when needed.
    """
    counter_1=0#used to keep calling options until 4 is returned from function.
    counter_2=0#used to keep prompting user to enter valid value for rarity.
    while True: # to keep looping incase invalid option is entered.
        PROMPT = input("Enter file name: ")
        try:
            fp = open(PROMPT, "r") 
            break # to stop loop since valid option is entered
            
        except FileNotFoundError: #try-except used to prevent code crashing
            print("\nError opening file. Please try again.")
            continue
            
        fp = open(PROMPT, "r")
# above 13 lines is the equivilant of calling "open_file(), it was done this \
# way so that the variables are stored inside of main().        
    reader = csv.reader(fp)
    next(reader,None)
    data = []
    for line in reader:
        Name = line[0]
        Element = line[2]
        Weapon = line[3]
        Rarity = int(line[1])
        Region = line[4]
        tup = (Name,Element,Weapon,Rarity,Region or None) 
        data.append(tup)
# above 10 lines is the equivilant of calling "read_file(), it was done this \
# way so that the variables are stored inside of main().      
    while counter_1 == 0:
        x = get_option() #variable used to act as placeholder for user input. \
        # its name is completley arbitrary.
        if x == 4:
            counter_1 +=1
        # above 3 lines under if-statement effectivley end function if 4 is \
            # inputted in options menu using the counter.
        elif x ==1:
            print("\nRegions:")
            print(get_region_list(data)[0], end = ", ")
            print(get_region_list(data)[1], end = ", ")
            print(get_region_list(data)[2], end = ", ")
            print(get_region_list(data)[3])
        # above 5 lines present regions in formatted way.
            
        
        elif x == 2:

            try:
                criteriaz = input(CRITERIA_INPUT)
                criteriaz = int(criteriaz)
            except ValueError:
                print("")
                print(INVALID_INPUT)
                criteriaz = input(CRITERIA_INPUT)
            if 0 >= criteriaz or criteriaz > 4:
                print("")
                print(INVALID_INPUT)
                criteriaz = input(CRITERIA_INPUT) 
            else:
                while counter_2 == 0 and criteriaz == 3:
                    if criteriaz == 3:
                        try:
                            valuez = input(VALUE_INPUT)
                            valuez = int(valuez)
                            break
                        except ValueError:
                            print("")
                            print(INVALID_INPUT)
                            continue 
                            
            if criteriaz != 3:
                valuez = input(VALUE_INPUT)
                        
            # above lines under elif-statement, amke sure that after a user \
                # selects option 2 from "options", the user will select another \
                # int to specify a criteria that they want to filter the \
                # results on, where each number represents a criteria. If input \
                # is invalid, an error message is presented and code loops unti \
                # valid option is entered.
            c_by_con = get_characters_by_criterion(data,criteriaz, valuez)
            if c_by_con != []:
                list(c_by_con)
                a = "Character"
                b = "Element"
                c = "Weapon"
                d = "Rarity"
                e = "Region"
                print("\n{:20s}{:10s}{:10s}{:<10s}{:25s}".format(a,b,c,d,e))
                # above variable names are arbitrary, used to not exceed 80 \
                # character limit
                for element in c_by_con:
                    element = list(element) # converts tuple elements to list \
                    # so that they become mutable
                    if element[4] == None:
                        element[4] = "N/A"
                    if element[3] == 5:
                        print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(element[0], element[1], element[2], element[3], element[4]))
                        # the purpose of this if-statement was to sort characters \
                        # and list them based on raeity value in decsending order \
                        # so first, rarity of 5 is listed then rarity of 4 is done.
                for element in c_by_con:
                    element = list(element)
                    if element[4] == None:
                        element[4] = "N/A"
                    if element[3] == 4:
                        print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(element[0], element[1], element[2], element[3], element[4]))
                        # the purpose of this if-statement was to sort characters \
                        # and list them based on raeity value in decsending order \
                        # so first, rarity of 5 is listed then rarity of 4 is done.
            # Note for this function, rarity values were assumed to be 5 and 4 \
            # only, and no other values for rarity were taken into account. \
            # This way of sorting the items does work and is efficent for 2 \
            # values for rarity.
            else: #if empty list.
                print("")
                print("Nothing to print.")
                
        elif x == 3:
            elemente = input(ELEMENT_INPUT)
            weaponz = input(WEAPON_INPUT)
            # value inputs for criteria
            while True: #keeps looping to ensure valid values are entered.
                try:
                    raritiez = input(RARITY_INPUT)
                    raritiez = int(raritiez)
                    break
                except ValueError:
                    print("")
                    print("Invalid input")
                    continue #return back to loop
            ch_by_c = get_characters_by_criteria(data, elemente, weaponz, raritiez)
            # above line calls function get_characters_by_criteria.
            if ch_by_c == []:
                print("")
                print("Nothing to print.")
            else:
                display_characters(ch_by_c)
# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
# =============================================================================
if __name__ == "__main__":
    main()