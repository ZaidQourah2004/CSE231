# =============================================================================
# Project 9
# This program will use lists, sets, tuples, dictionaries and functions to \
# open and read "prices" file and "securities" file. Both files contain data \
# that relates to NYSTE from 2010-2016 and more specifically company stocks \
# and company codes. This program examines data from about 2010-2016 and making \ 
# a program that displays some information to the user. Using several functions \
# This program finds the maximum stock price of a user-chosen company on the NYSE \
# between 2010-2016. This program also finds the company in the whole NYSTE with \
# the highest stock price between 2010-2016. This program also finds the average \
# stock price of a user chosen company in the NYSE from 2010-2016. This program \
# is also capable of displaying all the companies names and their symbols in the \
# NYSE. Error messages are displayed when applicable. All these functions are put \
# in "main()", which displays a menu of options and interacts with the user until \
# the user chooses option 6 (quit).
#
#
# =============================================================================

import csv # to read csv files

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    """
    This function opens both prices and securities file. It takes no parameters\
    but it returns both filepointers for security and prices files. While loop \
    is written twice to try to keep opening the correct secuirty file and the correct\
    prices file.
    """
    while True: #keeps looping until correct file is opened.
        price_file_input = input("\nEnter the price's filename: ")
        try:
            fp_prices = open(price_file_input, 'r') # opens file
            break
        except:
            print("\nFile not found. Please try again.")
            continue
    
    while True: #keeps looping until correct file is opened.
        security_file_input = input("\nEnter the security's filename: ")
        try:
            fp_securities = open(security_file_input, 'r') # opens file
            break
        except:
            print("\nFile not found. Please try again.")
            continue
            
    return(fp_prices, fp_securities)

def read_file(securities_fp):
    """
    This function takes the securities filepointer as a parameter and opens the file\
    This function creates a set of all companies in the NYSTE, and also a dictionary \
    of information regarding each company using the info from the paramter.
    """
    fp = securities_fp
    company_names = list() # list of company names
    codes_list = [] # list of company symbols (key of dictionary)
    other_info_list = [] # list of info regarding each company (value for each key) 
    company_names_set = set() # set of all companies in the NYSTE
    
    reader = csv.reader(fp)
    next(reader,None) #skips header line as it is irrelevant
    
    for line in reader:
        company_names.append(line[0]) # appends name of company name
        codes_list.append(line[0]) # appends company symbol
        other_info_list.append(line[1:2] + line[3:7] + [[]]) #appends other info
        company_names_set.add(line[1]) # places all companies into a set
        


    companies_dict = zip(company_names, other_info_list) # company name is key,\
        # whilst other info is the value
    companies_dict = dict(companies_dict)
    
    return(company_names_set, companies_dict)
        

def add_prices(master_dictionary, prices_file_pointer):
    """
    This function takes 2 parameters (master_dictionary and prices filepointer)\
    This function does not return anything but the only thing it does is add \
    information from the file pointer into the 5th index of each list into each \
    value, so that the information in the master_dictionary would contain stock \
    prices.
    """
    fp = prices_file_pointer
    reader = csv.reader(fp)
    next(reader,None) #skips header line as it is irrelevant

    
    for line in reader:
        line[2] = float(line[2])
        line[3] = float(line[3])
        line[4] = float(line[4])
        line[5] = float(line[5])
        for key, value in master_dictionary.items():
            if line[1] == key:
                master_dictionary[key][5].append(line[0:1] + line[2:6])



def add_pricez(master_dictionary, prices_file_pointer):
    """
    This function is identical to "add_prices" function, but what it does is \
    return the master_dictionary at the end.
    """
    fp = prices_file_pointer
    reader = csv.reader(fp)
    next(reader,None) #skips header line as it is irrelevant

    
    for line in reader:
        line[2] = float(line[2])
        line[3] = float(line[3])
        line[4] = float(line[4])
        line[5] = float(line[5])
        for key, value in master_dictionary.items():
            if line[1] == key:
                master_dictionary[key][5].append(line[0:1] + line[2:6])
                
                
    return master_dictionary
def get_max_price_of_company (master_dictionary, company_symbol):
    """
    This function takes in 2 parameters (master_dictionary and company_symbol) \
    This function looks at all the keys in the master_dictionary and looks at the\
    key-value pair that's key is the company symbol parameter. Then this function\
    looks at all the lists in the value and finds the maximum stock price for \
    the company across all dates from 2010-2016. This function returns tuple of \
    company_symbol and its maximum price.
    """
    max_price_list = [] #stores all the stock prices of the company
    final_list = [] # narrows down max_price_list to find the maximum stock price \
    # and its associated date/dates
    
    for key, value in master_dictionary.items():
        if key != company_symbol:
            pass
        else:
            max_price = -1 # algorithim to find maximum price
            for element in value[5]:
                if element[4] > max_price:
                    max_price = element[4]
    for key, value in master_dictionary.items():
        if key != company_symbol:
            pass
        else:
            for element in value[5]:
                if element[4] == max_price:
                    max_price_list.append(element)
    
    x = sorted(max_price_list) #sorts list by date
    
    try:
        final_list.append(max_price)
    except:
        final_list.append(None) # if there is no stock price info available for\
            # company_symbol
    try:
        final_list.append((x[-1][0]))
    except:
        final_list.append(None)# if there is no stock price info available for\
            # company_symbol

    return(tuple(final_list))

def find_max_company_price (master_dictionary):
    """
    This function finds the maximum stock price in NYSTE from 2010-2016 for all\
    companies. This function takes the master_dictionary list as parameter and \
    returns the a tuple of company symbol and max price.
    """
    max_list = []
    max_price = -1 # algorithim to find maximum price.
    final_listtup = [] # this will be appended with company_symbol and max price\
        # then converted to a tuple
    for key, value in master_dictionary.items():
        if value[5] != []:
            for element in value[5]:
                if element[4] > max_price:
                    max_price = element[4]

    for key, value in master_dictionary.items():
        if value[5] != []:
            for element in value[5]:
                if element[4] == max_price:
                    element.append(key)
                    max_list.append(element)
    
    
    if len(max_list) > 1:
        x = (sorted(max_list)) # this was done in case there were multiple dates\
            #where the same company had the same max stock price. So it was sorted\
            # and the company with the highest date was inputted into the final tuple.
    else: # if there is only one unique option
        tup = []
        tup.append(max_list[0][-1])
        tup.append(max_list[0][-2])
        tup = tuple(tup)
        return tup
        
    final_listtup.append(x[-1][-1])
    final_listtup.append(x[-1][-2])
    final_listtup = tuple(final_listtup)
    return(final_listtup)
    # the above 4 lines relate to the if-statement.



def get_avg_price_of_company (master_dictionary, company_symbol):
    """
    This function takes in 2 parameters (master_dictionary and company_symbol) \
    This function looks at all the keys in the master_dictionary and looks at the\
    key-value pair that's key is the company symbol parameter. Then this function\
    looks at all the lists in the value and finds the average stock price for \
    the company across all dates from 2010-2016. This function returns tuple of \
    company_symbol and its average price.
    """
    final_list = []
    
    for key, value in master_dictionary.items():
        if key != company_symbol:
            pass
        else:
            for element in value[5]:
                final_list.append(element[4]) #adds all prices of the company to\
                # final list
                
    try:
        avg = round(sum(final_list) / len(final_list), 2)
    except:
        avg = 0.0
    
    return(float(avg))
    

def display_list_105(lst):  # "{:^105s}"
    """
    This function displays all elements in a list (that contains 3 elements) as\
    strings. This function has a main list as a parameter, and it returns nothing.
    """
    x = 0 # counter. variable name is arbitrary
    listz = []
    lst = sorted(lst) # sorts all elements alphabetically
    try:
        for i in range(len(lst)): # goes through entier list of lists
            y = lst[x:x+3] # prints every 3 elements
            if y != []:
                    listz.append(y)
            x += 3 # so that an element is not printed more than once.
    except:
        pass
    for listt in listz:
        if len(listt) == 3:
            print("{:^35s}{:^35s}{:^35s}".format(listt[0], listt[1], listt[2]))
        elif len(listt) == 2:
            print("{:^35s}{:^35s}".format(listt[0],listt[1]))
        elif len(listt) == 1:
            print("{:^35s}".format(listt[0]))

    if (len(listz[-1])) == 1:
        print("")
    elif (len(listz[-1])) == 3:
        print("")
        print("")
        
def main():
    """
    Main is a function that takes no parameter and it interacts with the user.\
    It contains 6 options to choose from, and each individual option represents\
    one of the functions written previously in the code. The 6th option is quit\
    and when selected the program ends (while loop stops looping.)
    """
    print(WELCOME)
    
    fp = open_file()
    
    prices = fp[0]
    
    securities = fp[1]
    
    read_securities = read_file(securities)
    
    company_names = sorted(read_securities[0]) # sorts company names alphabetically.
    
    master_dict = (read_securities[1])
    
    master_dictz = add_pricez(master_dict, prices)
    
    companies_symbols_list = []

    
    option = -5 # intialize options variable
    
    while option != 6:
        print(MENU)
        while True:
            try:
                option = int(input("\nOption: "))
                if 1 <= option <= 6:
                    break
                else:
                    print("\nInvalid option. Please try again.")
                    continue

            except:
                print("\nInvalid option. Please try again.")
                continue
        # the above try-except statement makes sure that user input for options\
        # is an int from 1-6.
        if option == 1:
            print("")
            print("                        Companies in the New York Stock Market from 2010 to 2016                         ")
            display_list_105(company_names)

        
        elif option == 2:
            print("\ncompanies' symbols:")
            for key, value in master_dict.items():
                companies_symbols_list.append(key)
            display_list_105(companies_symbols_list)


        elif option == 3:
            
            while True:
                
                company_symbol = input("\nEnter company symbol for max price: ")
                
                if company_symbol not in master_dictz:
                    print("\nError: not a company symbol. Please try again.")
                    continue
                else:
                    break
            x = get_max_price_of_company(master_dictz, company_symbol)
            
            if x[0] == -1: # this value is the initial value for max_price in \
                # original function, meaning that if it is unchanged then there\
                # was no max_price detected.
                print("\nThere were no prices.")
            else:
                print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(x[0], x[1]))
                    
        elif option == 4:
            
            y = find_max_company_price(master_dictz)
            
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(y[0], y[1]))
        
        elif option == 5:       
            while True:
                
                company_symbol = input("\nEnter company symbol for average price: ")
                
                if company_symbol not in master_dictz:
                    print("\nError: not a company symbol. Please try again.")
                    continue
                else:
                    break
            z = get_avg_price_of_company(master_dictz, company_symbol)
            print("\nThe average stock price was ${:.2f}.\n".format(z))
                  
if __name__ == "__main__": 
    main() 
