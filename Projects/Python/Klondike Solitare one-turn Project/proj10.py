# =============================================================================
# Project 10
#
# The objective of this project is to use a the classes Card and Deck to create \
# a Klondike one-turn solitare game. this is done by creating functions that use \
# the built in methods in the Deck and Card classes. The game is created by \
# initialzing the board at the start as per the game rules. A second function was \
# created to display rhe board in presentable way so that the user can interact \ 
# with the board with better understanding of the current state of the game. \
# Several functions were created to deal cards and move them from one part of \
# the board to other sucesfully as per game rules. This includes stock to waste, \
# waste to tableau, waste to foundation, tableau to tableau, tableau to foundation \
# A check-win function was created to check the current condition of the board \
# returns True if board is in winning state, else returns False. A parse option \
# function was created to check i a user input is valid or not, if it is it returns \
# a list of the move that the user was trying to make, else it returns None. All \
# of these functions were used to create the main() function which is the game \
# and it is the functions that uses all of the previously mentioned function to \
# create the game.    
# =============================================================================


from cards import Card, Deck
import sys # to quit program and stop running code.

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    """
    This function does not have a parameter and at the end it returns the starting \
    state of a Klondike Turn one Solitare game, where the tableau, foundation, stock \
    pile and waste pile are returned.
    """
    stock = Deck() # creates deck     
    
    stock.shuffle() # shuffles deck     

    
    tableau = [[],[],[],[],[],[],[]] # initializes 7 empty lists (7 empty tableaus)
    for i in range(7): # going through each tableau
        for j in range(i,7): # done so that tableau 1 would have 1 card, tableau \
            # 2 would have 2 cards, etc.. until tableau 7 is reached. Tableau 7 \
            # contains 7 cards. There are 28 cards in total in all Tableus initially.
            card = stock.deal() # gets top card from stock pile
            tableau[j].append(card) # adds the top card from stock pile to tableau.
    for tab in tableau:
        for card in tab: # flips all cards downwards for all tableaus.
            card.flip_card()
    for tab in tableau:
        tab[-1].flip_card() # only flips the top card upwards for each tableau.
    
    top_card = stock.deal() # gets top card from stock pile

    waste = []
    waste.append(top_card) # adds top card from stock pile to waste.
    foundation = [[],[],[],[]] # initializes foundation.
    return(tableau, stock, foundation, waste)

    
    
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    """
    This function takes the list of cards in the stock pile and the list of cards \
    in the waste pile and uses both parameters to move cards from the stock pile to \
    the waste pile. This function returns True if the move was possible, else returns \
    false.
    """
    if len(stock) > 0: # checks if stock is not empty
        waste.append(stock.deal()) # gets top card in stock pile and adds it to \
        # waste pile.
        return True # if move can be made
    else:
        return False # if move cannot be made,
    
       
def waste_to_tableau( waste, tableau, t_num ):
    """
    This function takes the waste list, tableau (list containing 7 lists) and tableau \
    number (which acts an index number for tableau list). as parameters This attempts to move \
    top card from the waste pile to the specific tableau coulumn in tableau. \
    This function returns True if the move was possible, else returns false.   
    """
    if len(waste) > 0:
        last_card = waste[-1]
        if len(tableau[t_num]) == 0:
            if last_card.rank() == 13:
                tableau[t_num].append(waste.pop())
                return True
            else:
                return False
        # per game rules if tableau column is empty, the only card that can be \
        # inserted is a King card.
        last_card_tableau = tableau[t_num][-1]
        if last_card.suit() == 1 or last_card.suit() == 4:
            
            if last_card_tableau.suit() == 3 and last_card.rank() == last_card_tableau.rank() - 1 :
                    tableau[t_num].append(waste.pop())
                    return True


            elif last_card_tableau.suit() == 2 and last_card.rank() == last_card_tableau.rank() - 1 :
                    tableau[t_num].append(waste.pop())
                    return True
            else:
                return False
        if last_card.suit() == 3 or last_card.suit() == 2:
            if last_card_tableau.suit() == 1 and last_card.rank() == last_card_tableau.rank() - 1 :
                    tableau[t_num].append(waste.pop())
                    return True


            if last_card_tableau.suit() == 4 and last_card.rank() == last_card_tableau.rank() - 1 :
                    tableau[t_num].append(waste.pop())
                    return True

            else:
                return False
        # The two above if statements check the color and rank of the card in the \
        # specified tableau column. It compares this information with the rank and \
        # color of the top card in the waste pile. If card in waste pile is of opposite \
        # color and one less rank then the card can be added to the tableau else \
        # it cannot and hence the function returns False.
        return False # if none of the conditions are met

    return False # if there are no cards in waste pile.



def waste_to_foundation( waste, foundation, f_num ):
    """
    This function takes the waste list, foundation (list containing 4 lists) and \ 
    foundation number (which acts an index number for foundation list) as parameters. This \ 
    attempts to move top card from the waste pile to the specific tableau coulumn \ 
    in foundation. This function returns True if the move was possible, else \ 
    returns false.   
    """
    if len(waste) > 0:
        last_card = waste[-1]
        if len(foundation[f_num]) == 0:
            if last_card.rank() != 1: 
                return False
            else:

                foundation[f_num].append(waste.pop())
                return True
        # if foundation column is empty only an Ace is allowed
        last_card_foundation = foundation[f_num][-1]
        if last_card.suit() == last_card_foundation.suit() and last_card.rank() == last_card_foundation.rank() + 1 :
                foundation[f_num].append(waste.pop())
                return True
        # looks at each foundation column and adds cards assendingly. ie: A, 2, 3 etc..
    return False # if card cannot be added.


def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    """
    This function takes the tableau and tableau column number as well as the \
    foundation and foundation column number as parameters. This function will \
    return True if the move is valid, otherwise returns False.
    """
    if len(tableau[t_num]) > 0: # checks if tableau column has any cards
        last_card = tableau[t_num][-1]
        if len(foundation[f_num]) == 0: # if foundation is empty
            if last_card.rank() != 1: # if card is not an Ace.
                return False
            else:

                foundation[f_num].append((tableau[t_num]).pop()) # adds card
                if tableau[t_num] != [] and tableau[t_num][-1].is_face_up() == False:
                    tableau[t_num][-1].flip_card() # makes sure that the top card
                    # in tableau column is face up.
                return True

        last_card_foundation = foundation[f_num][-1]
        if last_card.suit() == last_card_foundation.suit() and last_card.rank() == last_card_foundation.rank() + 1 :
                foundation[f_num].append((tableau[t_num]).pop())
                if tableau[t_num] != [] and tableau[t_num][-1].is_face_up() == False:
                    tableau[t_num][-1].flip_card() # makes sure that the top card
                    # in tableau column is face up.
                return True
        # the above if-statement is executed if foundation column already contains \
        # at least one card.
    return False

def tableau_to_tableau( tableau, t_num1, t_num2 ):
    """
    This function takes the tableau and two tableau column numbers as parameters. \
    This function will attempt to move a card from one tableau to another. \
    This function will return True if the move is valid, otherwise returns False. \
    """
    if len(tableau[t_num1]) > 0:
         last_card = tableau[t_num1][-1]
         if len(tableau[t_num2]) == 0:
             if last_card.rank() == 13: # only King can be inserted as its empty.
                 tableau[t_num2].append(tableau[t_num1].pop())
                 if tableau[t_num1] != [] and tableau[t_num1][-1].is_face_up() == False:
                     tableau[t_num1][-1].flip_card() # flips top card in tableau \
                        # that lost a card.
                 return True
             else:
                 return False
         last_card_tableau = tableau[t_num2][-1]
         if last_card.suit() == 1 or last_card.suit() == 4:
             
             if last_card_tableau.suit() == 3 and last_card.rank() == last_card_tableau.rank() - 1 :
                     tableau[t_num2].append(tableau[t_num1].pop())
                     if tableau[t_num1] != [] and tableau[t_num1][-1].is_face_up() == False:
                         tableau[t_num1][-1].flip_card()
                     return True
 
 
             elif last_card_tableau.suit() == 2 and last_card.rank() == last_card_tableau.rank() - 1 :
                     tableau[t_num2].append(tableau[t_num1].pop())
                     if tableau[t_num1] != [] and tableau[t_num1][-1].is_face_up() == False:
                         tableau[t_num1][-1].flip_card()
                     return True
             else:
                 return False
         if last_card.suit() == 3 or last_card.suit() == 2:
             if last_card_tableau.suit() == 1 and last_card.rank() == last_card_tableau.rank() - 1 :
                     tableau[t_num2].append(tableau[t_num1].pop())
                     if tableau[t_num1] != [] and tableau[t_num1][-1].is_face_up() == False:
                         tableau[t_num1][-1].flip_card()
                     return True
 
 
             if last_card_tableau.suit() == 4 and last_card.rank() == last_card_tableau.rank() - 1 :
                     tableau[t_num2].append(tableau[t_num1].pop())
                     if tableau[t_num1] != [] and tableau[t_num1][-1].is_face_up() == False:
                         tableau[t_num1][-1].flip_card()
                     return True
                 
        # The 4 above if statements check the color and rank of the card in the \
        # specified tableau column. It compares this information with the rank and \
        # color of the top card in the other tableau pile. If card in tableau pile \
        # is of opposite color and one less rank then the card can be added to \ 
        # the other tableau column, else it cannot and hence the function returns \ 
        # False.
 
             else:
                 return False
         return False

def check_win (stock, waste, foundation, tableau):
    """
    This function takes the stock pile, waste pile, foundation and tableau as \
    parameters and checks if the game is in a winning state or not. If it is \
    then True is returned, else False is returned.
    """
    if len(waste) != 0:
        return False
    if tableau != [[],[],[],[],[],[],[]]:
        return False

    if len(stock) != 0:
        return False
    return True

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():
    """
    This function does not take a parameter and does not return anything. This \
    function interacts with the user and makes use of the previous functions to \
    create the Klondike one turn Solitare game.
    """
    option = "x" # initialize variable
    while option != "Q":
        inital_deck = initialize() # calls function.
        print(MENU)
        display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
        # above displays original deck
        INPUT = "CSE 231" # initializing variable.
        while check_win(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3]) == False or INPUT != "Q":
            INPUT = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
            option = parse_option(INPUT)

            if option == None: # if the option is not valid (not in menu)
                display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                continue
            elif option[0] == "TT":
                tableau_2_tableau = tableau_to_tableau(inital_deck[0], option[1] - 1, option[2] - 1)
                if tableau_2_tableau == False:
                    print("\nInvalid move!\n")
                display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                
            elif option[0] == "TF":
                tableau_2_foundation = tableau_to_foundation(inital_deck[0], inital_deck[2], option[1] - 1, option[2] - 1)
                if tableau_2_foundation == False:
                    print("\nInvalid move!\n")
                    display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                else:
                    win_loss = check_win(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                    if win_loss == False:
                        display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                      
                    else:
                        print("You won!")
                        display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                        break # the game ends
                        
                  
            elif option[0] == "WT":
                waste_2_tab = waste_to_tableau(inital_deck[3], inital_deck[0], option[1] - 1)
                if waste_2_tab == False: # if move cannot be executed
                    print("\nInvalid move!\n")
    
                display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                
            elif option[0] == "WF":
                waste_2_foundation = waste_to_foundation(inital_deck[3], inital_deck[2], option[1] - 1)
                if waste_2_foundation == False:
                    print("\nInvalid move!\n")
                else:
                     win_loss = check_win(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                     if win_loss == False:
                         display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                       
                     else:
                         print("You won!")
                         display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
                         break
            elif option[0] == "SW":
                stock_2_waste = stock_to_waste(inital_deck[1], inital_deck[3])
                if stock_2_waste == False:
                    print("\nInvalid move!\n")
                else:
                    display(inital_deck[0], inital_deck[1], inital_deck[2], inital_deck[3])
            #elif option[0] == "R": # restarts the game and re-initializes the board
                    #continue
            elif option[0] == "H":
                print(MENU)
            elif option[0] == "Q": # quits the game and program ends.
                sys.exit()
            elif option[0] == "R":
                break # causes currnet loop to end so goes to main loop which \
                # causes game to restart and re-shuffle cards.

    # Since all / most functions return a boolean, when the function \
    # that is being executed does not return False (ie: return True) then \
    # the move will be excecuted.
if __name__ == '__main__':
     main()
