#############################################################################
# Project 8
# The objective of this project is to use lists and dictionaries to extract \
# some data from a network of friends. This data includes people's names and \
# the names of their friends. This data can be then manipulated using lists \
# and dictionaries to find who has the most friends, the second friends of \
# each person, and the people who have the most friends in common. This \
# information can be extracted through the creation of multiple functions.
# This project opens and reads a csv and txt file and then different types \
# of informations can be extracted from these files and the different functions. \
# Main() is the function that will interact with the user, and it interacts \
# with the user and allows user to choose from 4 different options which are \
# practically the functions that were created. Some of the options interact \
# with the user as they prompt the user to enter a name of a valid person. \
# Error messages are shown in main when nessacary and if user input does not \
# match what is expected.
#############################################################################

MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
import csv # to read csv files

def open_file(s):
    """
    This function takes the string "s" as a parameter, and prints a string \
    inside an input to prompt the user to open a specific file which is 
    indicated by "s". This function keeps looping until a valid filename \
    entered, and an error message is displayed if a wrong filename is \
    inputted. The function returns filepointer "fp", which opens the file.
                                                            
    """
    while True:
        filename = input("\nInput a {} file: ".format(s))
        try:
            fp = open(filename, 'r', encoding = "windows-1252") #encoding used \
                # to open ".txt" files so info in files is preserved.
            break
        except FileNotFoundError:
            print("\nError in opening file.")
            continue
    return fp

def read_names(fp):
    """
     This function reads the names and appends each line (which is a name of
     one person) into a list which is called "list_of_names" to store names
     of the human. "fp" is a paramter and isued to open the file.
    """
    list_of_names = []
    reader = csv.reader(fp)
    for line in reader: # iterates through file
        line = line[0]
        list_of_names.append(line)
    return(list_of_names)


def read_friends(fp, names_lst):
    """
     This function reads the names and appends each line (which is a list of
     numbers with types string. Each element in a line represents a name of
     a person and then the objective of the function is to return a list of
     lists of the friends of each person. "fp" and the names list are the
     parameters for this function as fp is used to open the friends file \
     and the names list is used to get the correct indexes for each person.
    """
    reader = csv.reader(fp)
    listt = [] # main list that stores the "mini lists" inside of it.

    
    for index, line in enumerate(reader):
        line = line[:-1] # ignores trailing commas after each string
        listt.append([])
        for i, element in enumerate(line): # enumerate needed to get index \
        # number of each person so that the friends list matches the right \
        # human
            listt[index].append(names_lst[int(element)]) # each str is \
            # converted to an int then locates the name of each friend using \
            # that number, and adds it to corresponding "mini list" based on \
            # index number.
    return (listt)
    

def create_friends_dict(names_lst,friends_lst):
    """
    This functions creates a dictionary where it stores each person's name 
    as a key and the list of that person as a value (thus a key-valie pair).
    This was achieved through the "zip function". The list of names and list
    of friends were needed as parameters, and this function then returns
    the friends_dict. 
    """
    dict_of_friends = zip(names_lst, friends_lst)


    return (dict(dict_of_friends))
       
def find_common_friends(name1, name2, friends_dict):
    """
    This function takes 2 names as parameters to compare them using the third
    paramter friends_dict. the values of each key will be compared in the dictionary
    and then a set is created to insert all the mutual (common) friends.
    The set of common friends is returned.
    """
    set_of_friends = set() # this set will take all the friends (mutal or not)
    set_of_common_friends = set() # this set will filter out the above set \
    # to find names that are friends with both names.
    
    for key, val in friends_dict.items():
        if key == name1 or key == name2:
            for element in val:
                set_of_friends.add(element)
    
    for element in set_of_friends:
        if element in friends_dict[name1] and element in friends_dict[name2]:
            set_of_common_friends.add(element)
        else:
            pass
    return(set_of_common_friends)

def find_max_friends(names_lst, friends_lst):
    """
    This function finds the names of the people who have the most friends.
    The first part of this function find a dictionary of each person and 
    a list of their friends; then the length of each list is stored and 
    the highest value is stored. Each key-value pair in the dictionary will
    be reviewed and the lengths of each item in the dict will be compared
    and the key/s of the longest list will be added to a list. This function
    returns the list and also the maximum number of friends. 
    """
    maximum = -1 # used to make an algorithim to find the maximum value of friends.
    
    friends_dict = zip(names_lst, friends_lst)
    friends_dict = dict(friends_dict)
    list_of_max = []
    
    for key, val in friends_dict.items():
        if len(val) > maximum:
            maximum = len(val)
    
    for key, val in friends_dict.items():
        if len(val) == maximum:
            list_of_max.append(key)
    list_of_max.sort() # sorts names in alphabetical order
    return(list_of_max, maximum)

    
def find_max_common_friends(friends_dict):
    """
    This function takes the friends dictionary and finds which pairs of
    people have the most friends in common. It returns a list of those
    pairs with the most common friends and how many friends they have.
    Each pair is represented as a tuple of names (strings).
    The tuples are sorted alphabetically then the list is returned along with
    maximum value.
    """
    list_of_pairs = [] # finds all possible names pairing
    list_of_mcf = [] # stores only the pairs that have the max common friends
    for keyz, value in friends_dict.items():
        for key, val in friends_dict.items(): # checks each friend for each 
        #person
            if keyz == key:
                continue
            if (key, keyz) not in list_of_pairs:
                list_of_pairs.append((keyz, key))
            
    maximum = -5 # used to make max-level algorithim.
        
    for pair in list_of_pairs:
        if (len(find_common_friends(pair[0], pair[1], friends_dict))) > maximum:
            maximum = (len(find_common_friends(pair[0], pair[1], friends_dict))) # finds maximum value of common friends
    for pair in list_of_pairs:
        if (len(find_common_friends(pair[0], pair[1], friends_dict))) == maximum: # sees which pair has the maximum value then appends it
        # to the list
            list_of_mcf.append(pair)
            
    return(list_of_mcf, maximum)
    
def find_second_friends(friends_dict): 
    """
    This function finds the second friends of every person. This is done by \
    looking at each key, value item in the dictionary and replacing each element
    in each value by the friends of that person using indexes and slicing.
    This function takes friends_dict as a parameter and returns the another
    dictionary which indicates the second friends of each person.
    """
    dictt = {}

    for key, value in friends_dict.items():
        dictt[key] = set() # so names are not repeated more than once
        for name in value:
            for secondfriendz in friends_dict[name]:
                if secondfriendz != key and secondfriendz not in friends_dict[key]: # so a person would not be considered their own 
                # second friend
                    dictt[key].add(secondfriendz)
    return(dictt)
                

def find_max_second_friends(seconds_dict):
    """
    This function uses the information from the second friends dictionary and
    finds the name/s (through key, value pair) with the most second friends
    using an algorithim. The names list is returned along with the max no, of
    friends.
    """
    max_names = [] # list of names with most second friends
    maximum = -1 # used to find maximum number of second friends.
    for key, val in seconds_dict.items(): # checks each item in dict and sees
    # which one has the highest length for its value in key, value pair.
        if len(val) > maximum:
            maximum = len(val)
    for key, val in seconds_dict.items(): # checks if length of value in key
    # value pair is equal to maximum length; if so it is added to list.
        if len(val) == maximum:
            max_names.append(key)
            
    return((max_names, maximum))

def main():
    """
    Main() is the function that will interact with the user, and it interacts \ 
    with the user and allows user to choose from 4 different options which are \
    practically the functions that were created. Some of the options interact \
    with the user as they prompt the user to enter a name of a valid person. \
    Error messages are shown in main when nessacary and if user input does not \
    match what is expected.
    """
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)
    # above lines open and read files and call functions created.

    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5': # if option is 5, the program quits/ends.

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4":
            while True:
                name = input("\nEnter a name: ")
                if name not in names_lst:
                    print("\nThe name {} is not in the list.".format(name))
                    continue
                else:
                    break
            print("\nFriends of {}:".format(name))
            for element in (friends_dict[name]):
                print(element)

        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()

