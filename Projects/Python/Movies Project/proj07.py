# =============================================================================
# Project 7
# The objective of this project is to open and read "windows 1252" files that \
# contain data regarding user reviews, info about users and a numbeer of movies.
# The data was sorted on year movie was pblished and genre of movie. This \
# program also filter out the users depending on their occupation. The \
# highest average rated movies and highest average ratings were also used. This \
# program also calculates the average rating of movies by a specific group of \
# users. For this to occur, some functions were created to achieve this \ 
# which will all be explained individually. These functions are then used \
# to create a bigger function "main()", which will interact with the user. \
# Main() will prompt the user to 3 files, (users, reviews and movies), then \
# after a valid file is opened a menu of options is displayed. The first option \
# allows user to view the highest rated movies for a specific year. Option 2 \
# allows the user to view the highest rated movie for a specific genre. Option
# 3 shows the highest rated movies by a specific gender, whereas option 4 \
# displays the highest rated movie by a specific occupation. Option 5 is \
# "Quit" and it ends the program running.
# =============================================================================


GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western'] #list of all valid genres,
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer'] # list
# of all valid occupations
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        ''' # string for menu
def open_file(s):
    """
    This function takes the string "s" as a parameter, and prints a string \
    inside an input to prompt the user to open a specific file which is 
    indicated by "s". This function keeps looping until a valid filename \
    entered, and an error message is displayed if a wrong filename is \
    inputted. The function returns filepointer "fp", which opens the file.
                                                            
    """
    while True:
        filename = input("\nInput {} filename: ".format(s))
        try:
            fp = open(filename, 'r', encoding = "windows-1252") #encoding used \
                # to open ".txt" files so info in files is preserved.
            break
        except FileNotFoundError:
            print("File not found! Try Again!")
            continue
    return fp


def read_reviews(N,fp):
    """
    This function reads the reviews file. It takes "N" and "fp" as parameters \
    where fp is the open_file function for the reviews file ONLY. N is the \
    length of user_file (it is an integer that represents the number of users).
    This function will have (N +1) empty lists inside it, and each list \
    starting from the second one (index 1). The list is sorted based on the \
    user ids. Each lis within the main list will include tuples that represent \
    the movie id and its rating sorted from lowest movie id rating to highest.
    This is done for all lists index 1 and upwards, and at the end the function \
    returns a list of lists of tuples of ints.
    """

    reviews_list = [] # main list
    
    for i in range(N+1):
        reviews_list.append([]) # (N + 1) lists inside of main list
    for line in fp:
        x = tuple(line.split('\t')) # to read lines correctly in neat way.
        userid = int(x[0])
        movieid = int(x[1])
        ratings = int(x[2])
        
    
        tuplz = (movieid, ratings) # tuples inside of list inside of main list.
        reviews_list[userid].append(tuplz) # puts the correct tuple inside of \
            # correct list in list.
        
    for i in reviews_list:
        i.sort() #sorts tuples
    return reviews_list
    


def read_users(fp):
   """
   This function reads the users file. It takes "fp" as a parameter, which is \
   the function that oepns users file. reviewer, age, gender and occupation \
   are what is inputted into the list. Data for each user is stored in a tuple.
   the user_list is returned by the function.
   """
   user_list = [[]] #list which stores users.

   for line in fp:
       x = (line.strip().split("|")) # organizes data
       x[1] = int(x[1])
       x[2] = str(x[2])
       x[3] = str(x[3])
       x[4] = str(x[4])
       # above 4 lines makes the data into correct type.
       x = tuple(x) # converts each user into a tuple
       user_list.append(x[1:4]) # adds, reviewer, age, gender, occupation.
       
   return user_list


def read_movies(fp):
    """
    This function reads the movies file. It takes "fp" as a parameter, which is \
    the function that oepns movies file. title, date and list of genres\
    are what is inputted into the list. Data for each movie is stored in a tuple.
    the movie_list is returned by the function.
    """
    movies_list = [[]] # list which stores movies.
    for line in fp: # reads through file
        genres_int = [] # stores genres
        final_genres_list = [] # puts genres_int list in correct oder.
        x = (line.strip().split("|")) # organizes lines in file.
        Title = x[1]
        Date = x[2]
        Genre = x[5:]
        for i in Genre:
            i_int = int(i)
            genres_int.append(i_int) # adds either 1 or 0 if movie has a specific \
                # genre or not.
        for i, value in enumerate(genres_int):
            if value == 1:
                final_genres_list.append(GENRES[i]) # this if-statement \
                    # recognizes if movie is classified under a certain genre or \
                        # not.
        tup = (Title, Date, final_genres_list) # sorts information for each movie.
        movies_list.append(tup) # adds each movie as a tuple to main list
    return (movies_list)
        
def year_movies(year, L_movies): # This code was written after  a \
# teaching assistant explained psuedo-code to a group of students including \
# myself; this is why this function may be simmilar to that of other students
    """
    This function takes parameters "year" and "L_movies" as parameters, and \
    this function basically differentiates between all movies and sees when \
    each movie was released based on the list of movies provided "L_movies". \
    Then this function uses "year" to see the index of each movie that was \
    released in the same year as parameter "year" and sorts indexes from \
    highest to lowest.
    """
    m = []
    for i, tup in enumerate(L_movies[1:],1):
        # below line retrieves date
        date = tup[1]
        try:
            m_year = date.split("-")[-1] # removes dashes to convert str to int.
            m_year_int = int(m_year)
            if m_year_int == year:
                m.append(i) #appends index
        except ValueError:
            continue
    m.sort() # sorts indexes in the list
    return (m)
    
def genre_movies(genre, L_movies):
    """
    This function returns a sorted list of lists where each list is in the main list \
    This function filters the main movie list to find movies for a specific \
    genre and returns their ids as a list. The genre is filtered based on the \
    parameter genre, while L_movies is the list of movies that will be filtered.
    """
    m = [] # list that stores movie

    for i, tup in enumerate(L_movies[1:],1): # for loop iterates through file.


         if genre in tup[2]:
             m.append(i) # appends movie, if movie contains genre chosen.
    return (m)

def gen_users(gender, L_users, L_reviews):
    """
    This function returns a  list of lists where each list  is in the main list \
    This function filters the main movie list to find movies for a specific \
    gender and returns it as a list. The gender is filtered based on the \
    parameter gender, while L_movies is the list of movies that will be filtered.
    L_reviews is the third parameter and it is added in the end to each user \
    of the specified gender to show the review of each user of gender chosen.
    """
    m = [] #  main list

    for i, collection in enumerate(L_users):
        if gender in collection:
            m.append(L_reviews[i]) # appends reviews only if gender matches input.
    return (m)
          
def occ_users(occ, L_users, L_reviews):
    """
    This function returns a list of list of tuples where each list in the main list \
    This function filters the main reviews list to find records for a specific \
    occupational group of users and returns them as a list of lists of tuples.
    This function takes "occ" as input for occupation, and has users list and \
    reviews lists as the 2 other parameters to append the data to the list.
    """
    m = [] # main list

    for i, collection in enumerate(L_users):
        if occ in collection:
            m.append(L_reviews[i])
    # the above for loop reads through file and appends tuples of reviews if \
    # the occupation matches the occupation of reviewer matches "occ". 
    return (m)

def highest_rated_by_movie(L_in, L_reviews, N_movies): #used for option 1 in main
    """
    This function calculates the average rating for the reviews in L_reviews \
    list of the movies in L_in list and returns a list of the highest average\
    rated movies and the highest average. This function also has a third \
    parameter "N" is used add "N" lists within the lists.
    """
    data_sorted = [] # list that sorts movies by their index number
    important_info = [] # list of empty lists based on N_movies.
    list_of_ratings = [] # list that sorts ratings for each movies by index.
    # this same list then stores the data from "important_info" and pairs \
    # ratings and index number correctley.
    new_list = [] # new_list is practically list_of_ratings after all info \
    # was appended to list_of_ratings


    for i in range(N_movies):
        data_sorted.append([])
    


    for index, tup in enumerate(L_reviews):
        if tup == []:
            tup.append((0,0))
        if tup != []:
            try:
                for i, value in enumerate(tup):
                        data_sorted[value[0]].append(value) # appends movie id
            except IndexError:
                continue

    
    for i in range(len(data_sorted)):
        important_info.append([])
    
    for collection in data_sorted:
        counter = 0
        for tup in collection:
            counter += tup[1]
        ratings = (counter / len(collection))
        ratings = round(ratings,2)

        list_of_ratings.append([ratings])
    
    for i, collection in enumerate(list_of_ratings):
        collection.append(i)
    
    for collection in list_of_ratings:
        if collection[1] in L_in:
            new_list.append(collection)
    
    max_ = 0
    
    for collection in new_list:
        if collection[0] > max_:
            max_ = collection[0]
            
    list_of_maxes = []
    
    for collection in new_list:
        if collection[0] == max_:
            list_of_maxes.append(collection[1])
    
    return(list_of_maxes, max_)
             

def highest_rated_by_movie2(L_in, L_reviews, N_movies): # This code was written 
#after  a \
# teaching assistant explained psuedo-code to a group of students including \
# myself; this is why this function may be simmilar to that of other students
# used for option 2 in main
    """
    This function calculates the average rating for the reviews in L_reviews \
    list of the movies in L_in list and returns a list of the highest average\
    rated movies and the highest average. This function also has a third \
    parameter "N" is used add "N" lists within the lists.
    """
    totals = [0] * len(L_in) # calculates total ratings for each index
    n_times = [0] * len(L_in) # calculates number of ratings for each index
    averages = [0] * len(L_in) # totals / n_times
    
    for i in range(len(L_in)): # loops depending on inde number
        for j in L_reviews: # iterates through each review
            if j != []: # eveything under this if-statement checks each rating \
                # in each list so that calculations can be done for each movie.
                for k in j:
                    if L_in[i] == k[0]:
                        totals[i] += k[1]
                        n_times[i] += 1
    for i in range(len(L_in)):
        averages[i] = totals[i] / n_times[i]
 
    max_list = [] # list that will store index that contain max value
    maximum = - 1
    for i in range(len(averages)): # checks each rating to see if its the max value.
        if averages[i] > maximum:
            maximum = averages[i]
            max_list = []
        if averages[i] == maximum:
            max_list.append(L_in[i]) #adds index of movie if it has highest rating.
    maximum = round(maximum, 2) # rounds value for maximum by 2
    return (max_list, maximum)

def highest_rated_by_reviewer(L_in,N_movies):
    """
    This function calculates the average rating for movies by a specific group\
    of users (L_in) and returns a list of the highest average rated movies and\
    the highest average. This function also takes the number of movies \
    "N_movies" as a parameter which was used to iterate through data set. \
    """
    for i in range(N_movies + 1):
        totals = [0] * (N_movies + 1)
        n_times = [0] * (N_movies + 1)
        averages = [0] * (N_movies + 1)
    # the above three lines were used to calculate average rating by reviewer \
    # for each movie.
    for i in L_in:
        if i != []:
            for tup in i:
                if tup[1] != "":
                    totals[tup[0]] += tup[1]
                    n_times[tup[0]] += 1
        else:
            continue
    for i in range((N_movies + 1)):
        averages[i] = totals[i] / n_times[i] # calculates avereage rating
    max_list = []
    maximum = - 1 # max value algorithim used to update maximum rating.
    for i in range(len(averages)):
        if averages[i] > maximum:
            maximum = averages[i]
            max_list = []
        if averages[i] == maximum:
            max_list.append(i) # appends list by index if the average max \
                #rating is == to the rating of the movie.
    maximum = round(maximum, 2)
    return (max_list, maximum)

def highest_rated_by_reviewer2(L_in,N):
    """
    This function calculates the average rating for movies by a specific group\
    of users (L_in) and returns a list of the highest average rated movies and\
    the highest average. This function also takes the number of movies \
    "N_movies" as a parameter which was used to iterate through data set. \
    """

    m = [] # this list sorts the tuples in L_in by their movie_id
    list_of_ratings = []
    list_of_averages = []
    list_of_ids = []
    tup_value = -1 # this acts as a counter to store the maximum value for \
    # reviewer_id

    
    for collection in L_in:
        for tup in collection:
            m.append(tup)
    m = sorted(m)

    
    for tup in m:
        if tup[0] > tup_value:
            tup_value = tup[0]

    for i in range(tup_value + 1):
        list_of_ratings.append([]) #adds empty lists within the list, where \
        # the number of lists is determined by greatest movie_id
    
    for i, listt in enumerate(list_of_ratings):     
        for index, val in enumerate(m):
            if val[0] == i:
                listt.append(val) # appends each list of tuples into \
                # respective list based on reviewer_id number

    
    for collection in list_of_ratings:
        sum_ = 0
        for tup in collection:
            sum_ += tup[1]
        try:
            list_of_averages.append(round((sum_) / (len(collection)), 2))
        except ZeroDivisionError:
            list_of_averages.append(0.0)
        # above for loop finds the average rating by each reviewer
    maximum = -1 # this was used as a counter to store the maximum rating
    
    for element in list_of_averages:
        if element > maximum:
            maximum = element
            
    for i, element in enumerate(list_of_averages):
        if element == maximum:
            list_of_ids.append(i)
    # the above for loop was used to see which movies recieved the maximum \
    # rating
    return (list_of_ids, maximum)
    
                


def main():
    """
    Main() will prompt the user to 3 files, (users, reviews and movies), then \
    after a valid file is opened a menu of options is displayed. The first option \
    allows user to view the highest rated movies for a specific year. Option 2 \
    allows the user to view the highest rated movie for a specific genre. Option
    3 shows the highest rated movies by a specific gender, whereas option 4 \
    displays the highest rated movie by a specific occupation. Option 5 is \
    "Quit" and it ends the program running. This function takes no parameter.
    """
    
    option = 0 # initialize variable
    counter_1 = 0 # counter to keep certain parts of the code to loop continuisly
    users = open_file("users")
    reviews = open_file("reviews")
    movies = open_file("movies")
    L_users = read_users(users)
    L_reviews = read_reviews(len(L_users) - 1, reviews)
    L_movies = read_movies(movies)
    users.close()
    reviews.close()
    movies.close()
    print(MENU)
    while option != 5: # keeps looping until option 5 is chosen (which is quit)
        try:
            
            option = int(input("\nSelect an option (1-5): "))
            if option > 5 or option < 0:
                print("\nError: not a valid option.")
                continue
        except ValueError:
            continue
        
        if option == 1:
            counter_1 = 0
            while counter_1 == 0:
                try:
                    year = input('\nInput a year: ')
                    year = int(year)
                    
                    if year > 1998 or year < 1930:
                        print("\nError in year.")
                        continue
                    else:
                        counter_1 +=1
                        movies_year = year_movies(year, L_movies)
                        highest_movie = highest_rated_by_movie(movies_year, L_reviews, len(L_movies))
                        print('\nAvg max rating for the year is: {}'.format(highest_movie[1]))
                        movie_id = highest_movie[0]
                        for i in movie_id:  
                            print(L_movies[i][0]) # extracts movie name from movie_id
                            # and prints movie name
        
                except ValueError:
                    print("\nError in year.")
                    continue
          
                

        if option == 2:
            counter_1 = 0
            while counter_1 == 0:

                print('\nValid Genres are:  {}'.format(GENRES))
                genre = input('Input a genre: ')
                    
                if genre.capitalize() not in GENRES:
                    print("\nError in genre.")
                    continue
                else:
                    counter_1 +=1
                    movies_genre = genre_movies(genre.capitalize(), L_movies)
        
                    highest_movie = highest_rated_by_movie2(movies_genre, L_reviews, len(L_users) -1)
                    
                    print('\nAvg max rating for the Genre is: {}'.format(highest_movie[1]))
                    movie_id = L_movies[highest_movie[0][0]]
                 
                    for i in range (len(highest_movie[0])): 
                        print(L_movies[highest_movie[0][i]][0]) # extracts movie 
                        #name from movie_id and prints movie name
                    

        if option == 3:
            counter_1 = 0

            while counter_1 == 0:

                gender = input('\nInput a gender (M,F): ')
                gender = gender[0].capitalize()
                if gender == "F" or gender == "M":
                    counter_1 += 1
                    users_gen = gen_users(gender, L_users, L_reviews)
                    highest_reviewer = highest_rated_by_reviewer2(users_gen, len(L_users) -1)
                    print('\nAvg max rating for the Gender is: {}'.format(highest_reviewer[1]))
                    for i in range (len(highest_reviewer[0])): 
                        print(L_movies[highest_reviewer[0][i]][0]) # extracts movie 
                        #name from movie_id and prints movie name
                else:
                    print("\nError in gender.")
                    continue
        if option == 4:
            counter_1 = 0
            while counter_1 == 0:
                print('\nValid Occupatipns are:  {}'.format(OCCUPATIONS))
                occ = input('Input an occupation: ')
                occ = occ.lower()
                if occ in OCCUPATIONS:
                    counter_1 += 1
                    users_occ = occ_users(occ, L_users, L_reviews)
                    highest_reviewer = highest_rated_by_reviewer2(users_occ, len(L_users) - 1)
                    print('\nAvg max rating for the occupation is: {}'.format(highest_reviewer[1]))
                    for i in range (len(highest_reviewer[0])): 
                        print(L_movies[highest_reviewer[0][i]][0]) # extracts movie 
                        #/ name from movie_id and prints movie name
                else:
                    print("\nError in occupation.")
                    continue

if __name__ == "__main__":
    main()
                                           

                

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


