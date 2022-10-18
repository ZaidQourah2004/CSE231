###############################################################################
# Project 5
# 
# The objective of this project is to read mutliple files relating to \
# extrasolar planetary data. Several mathematics and physics formulae \
# were used to collect different types of data from the files where \
# information was extracted from to gather information about the \ 
# possibility of life-supporting planets outside of earth. For this to \
# be done; several functions were created. "open_file()" was created to \
# open a valid file and return an error if the user trys opening an invalid \
# file. This function keeps prompting the user to choose a file until a valid \
# one is entered. The second function created was "make_float(s)" which \
# accepts a parameter, and converts the parameter to a float if possible, else \
# it would return -1. A third function was created "get_density(mass, radius)" \
# which accepts 2 parameters the mass and adius of a planet to calculate its \
# density using a mathematical formula. A fourth function was created and its \
# "temp_in_range(axis, star_temp, star_radius, albedo, lower_bound, upper_bound)"\
# which was used to determine if the tempreature of a given planet was suitable \
# for humans to live on and survive. A fifth function was defined "get_dist_range()" \
# which prompts the user for a distance in light years to set a range for how much \
# information from the file should be extracted. If an invalid option is inputted; the \
# program will keep prompting the user until a valid option is written. "main()" is the \
# last function used, and it makes use of all previously mentioned functions to output \
# information such as: number of stars in the system with the most stars, number of \
# planets in the system with the most planets, average mass of the planets, rocky \
# planets and gaseous planets in circumstellar habitable zone (if applicable) \
# All this information is displayed at the end of the code after the user inputs \
# 2 valid inputs for the dist_range function and open_file() function.
###############################################################################

import math


def open_file():
    """
    Accepts user input, and adds extension ".csv" to user input to open file \
    Keep prompting the user until a valid filename is entered. "file_pointer" \
    is returned which opens a valid file.
    """


  
    PROMPT = input("Input data to open: ")

    PROMPT_x = PROMPT + ".csv"
    
    while True: # to keep looping incase invalid option is entered.
        try:
            file_pointer = open(PROMPT_x, "r") 
            break # to stop loop since valid option is entered
            
        except FileNotFoundError: #try-except used to prevent code crashing
            print("\nError: file not found.  Please try again.")
            PROMPT = input("Enter a file name: ")
            
            PROMPT_x = PROMPT + ".csv"
            while True: # to keep looping incase invalid option is entered.
                try:
                    file_pointer = open(PROMPT_x, "r") 
                    return file_pointer 
                    break
                except FileNotFoundError:
                    break
    return file_pointer
 
def make_float(s):
    """
    accepts 1 parameter, and attempts to convert that paramter to a float then return float \
    if unable to do so, the function will return -1 
    """
    try: #try-except used to prevent code from crahsing if the parameter cannot be converted \
    # to a float
        return float(s)
    except ValueError:
        return -1
  
def get_density(MASS, RADIUS):
    """
    this function returns density if the information for the mass and radius is available \
    (as in the main() function, the information for mass and radius will be extracted from \
    files. This function converts the units for mass and radius to appropriate units as per \
    the "SI system" 
    """
    EARTH_MASS =  5.972E+24    # kg
    EARTH_RADIUS = 6.371E+6    # meters
    if MASS > 0 or RADIUS > 0:
        VOLUME = (4 /3) * math.pi * RADIUS**3 * EARTH_RADIUS**3
        DENSITY = (MASS * EARTH_MASS) / VOLUME
        return DENSITY
    else:
        return -1

def temp_in_range(axis, star_temp, star_radius, albedo, lower_bound, upper_bound):
    """
    this function calculates the planet tempreature using parameters: albedo, axis distance, \
    and star_temp. All parameters are converted to SI units by using constants "AU", and \
    "Solar_Radius". lower_bound and upper_bound were used to check if the planet tempreature \
    was within a habitale range for humans.
    """
    SOLAR_RADIUS = 6.975E+8   # radius of star in meters
    AU = 1.496E+11            # distance earth to sun in meters
    new_r = star_radius * SOLAR_RADIUS
    denom = (2 * axis * AU) 
    planet_temp = star_temp * (new_r / denom)**0.5 * (1 - albedo)**0.25
    if (lower_bound) < (planet_temp) < (upper_bound):
        return True
    else:
        return False

def get_dist_range():
    """
    Function accepts input for distance (this is the maximum for the range of distances \
    that the calculations will occur for. if the distance is greater than the input of \
    this function, then the planet and all associated values will not be considred.
    """
    while True:
        distance = input("\nEnter maximum distance from Earth (light years): ")
        
        try:
            float(distance)
            if float(distance) < 0:
                print("\nError: Distance needs to be greater than 0.")
                continue
            else:
                distance = float(distance)
                return distance
                break
                  
        except ValueError:
            print("\nError: Distance needs to be a float.")
            continue

def main():
    """
    makes use of all previously mentioned functions to output \
    information such as: number of stars in the system with the most stars, number of \
    planets in the system with the most planets, average mass of the planets, rocky \
    planets and gaseous planets in circumstellar habitable zone (if applicable) \
    All this information is displayed at the end of the code after the user inputs \
    2 valid inputs for the dist_range function and open_file() function.
    """
        #Constants
    PI = math.pi   
    EARTH_MASS =  5.972E+24    # kg
    EARTH_RADIUS = 6.371E+6    # meters
    SOLAR_RADIUS = 6.975E+8    # radius of star in meters
    AU = 1.496E+11             # distance earth to sun in meters
    PARSEC_LY = 3.262
    

    print("Welcome to program that finds nearby exoplanets in circumstellar habitable zone.")
    fp = open_file() #calls open_file
    D = get_dist_range() # calls get_dist_range()

    PARSEC_LY = 3.262 #constant to convert units to SI units and to make calculations easier.
    total_planet_mass = 0 # this variable will keep track of the combined mass of all planets so \
    # that it can be used to calculate the average mass of the planets.
    min_planets = 101 #used to calculate algorithim for minimum amount of planets.
    max_planets = -3 #used to calculate algorithim for maximum amount of planets.
    min_stars = 105 #used to calculate algorithim for minimum amount of stars.
    max_stars = -7 #used to calculate algorithim for maximum amount of stars.
    planet_counter = 0 #counts number of planets, so that it can be used to calculate average \
    # mass of planets.
    habitable_counter = 0 #keeps track of habitable planets.
    c_rocky_d = 10000000000 #high number set, so that the value is changed. concept for this \
    #variable is simmilar to that of high-level maximum algorithim. Keeps track of the distance \
    # for closest rocky planet.
    c_gas_d = 1000000000000 #high number set, so that the value is changed. concept for this \
    #variable is simmilar to that of high-level maximum algorithim. Keeps track of the distance \
    # for closest gaseous planet.
    planet_name_rocky = "" #replaced with line[25:] of rocky planet closest to circumstellar \
    #habitable zone.
    planet_name_gas = "" #replaced with line[25:] of gaseous planet closest to circumstellar \
    #habitable zone.
    

    
    for line in fp: #checks each line in file
        
        albedo = 0.5
        upper_bound = 350
        lower_bound = 200

        
  
        sys_D = make_float(line[114:]) #distance for planets.
        if 0 >= sys_D or sys_D * PARSEC_LY >= D: #checks if distance in range or not.
            continue #skips the line and moves on to the next
        else:


            planet_mass = make_float(line[86:96])

    
            sys_D = make_float((line[114:]))

        


            if planet_mass > 0:
                total_planet_mass += planet_mass
                planet_counter += 1
                
    
    
            if max_stars < make_float(line[50:57]):
                max_stars = make_float(line[50:57])
                
            if max_planets < make_float(line[58:65]):
                max_planets = make_float(line[58:65]) 
        
            if min_stars > make_float(line[50:57]):
                min_stars = make_float(line[50:57])
                
            if min_planets > make_float(line[58:65]):
                min_planets = make_float(line[58:65])

            # the above 10 lines are the min and max algorithims for star and planets \
            # to indicate the maximum and minimum nuumber of stars and planets for each \
            # star and planet.
            try:
                planet_mass = make_float(line[86:96])
            except ValueError:
                planet_mass =-1
                
            try:
                planet_radius = make_float(line[78:85])
            except ValueError:
                planet_radius =-1
            
        density = get_density(planet_mass, planet_radius)
        axis = make_float(line[66:77])
        star_temp = make_float(line[97:105])
        star_radius = make_float(line[106:113])
        if axis > 0 and star_temp > 0 and star_radius > 0: # to ensure no negative value under \
        # square root.
            temp_in_range(axis, star_temp, star_radius, albedo, lower_bound, upper_bound) # calling\
            # function
            if temp_in_range(axis, star_temp, star_radius, albedo,lower_bound, upper_bound) == True:
                habitable_counter += 1
                if 0 < planet_mass < 10 or 0 < planet_radius < 1.5 or density > 2000:
                    if c_rocky_d > sys_D: 
                        c_rocky_d = sys_D # makes the value for c_rocky as small as possible \
                        # to be able to identify closest distance to habitable zone.
                        planet_name_rocky = line[:25]
                        line_fixer_rock = (make_float(line[114:]) * PARSEC_LY)
                        # the above variable fixes the units for the closest distance.
                else:
                    if c_gas_d > sys_D:
                        c_gas_d = sys_D # makes the value for c_gas as small as possible \
                        # to be able to identify closest distance to habitable zone.
                        planet_name_gas = line[:25]
                        line_fixer_gas = (make_float(line[114:]) * PARSEC_LY)
                        # the above variable fixes the units for the closest distance.
                        

           
                
    average_mass = total_planet_mass / planet_counter
    planet_name_rocky = planet_name_rocky.lstrip() #removes leading whitespace
    planet_name_gas = planet_name_gas.lstrip() #removes leading whitespace
    
    fp.close() #closes file

    print("\nNumber of stars in systems with the most stars: {:.0f}.".format(max_stars))
    print("Number of planets in systems with the most planets: {:.0f}.".format(max_planets))
    print("Average mass of the planets: {:.2f} Earth masses.".format(average_mass))
    print("Number of planets in circumstellar habitable zone: {}.".format(habitable_counter) )
    if c_rocky_d < 1000000:
        print("Closest rocky planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(planet_name_rocky, line_fixer_rock))
    else:
        print("No rocky planet in circumstellar habitable zone.")
    if c_gas_d < 10000:
        print("Closest gaseous planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(planet_name_gas, line_fixer_gas))


if __name__ == '__main__': 
    main()
