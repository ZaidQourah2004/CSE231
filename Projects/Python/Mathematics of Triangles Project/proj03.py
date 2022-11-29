#############################################################################
#  Project 3
#
# Print Banner then ask the user if they would like to play a game
#
# If user inputs "Y" or "y" allow user to input 3 lenghts for 3 \
#
# sides. If the triangle is valid, print out the user inputs then \ 
#
# show user angles in degrees and radians, then show the user the perimeter \
#
# and area of triangle, then lastly show user what types of triangle the \
#
# triangle chosen (triangle chosen is based on the 3 lengths input) is. \
#
# If values that produce no triangle or degenerate triangle is entered then \
#
# code just reloops.
#
# In all cases the code re-loops until the user inputs a character that \ 
#
# isn't "Y" or "y" which then the number of valid triangles entered showed \
#
# then game ends.
#
# while loop is used to allow the user to play as long as possible
#
# prompting the user to continue playing the game or not.
#
#############################################################################

import math

BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
print("")

num_valid = 0 # variable I created to keep count of valid triangles 

loop_fixer = 0 # variable I created to fix an issue where the the wrong \ 

# output would be produced if the first user input was a degenerate or \ 

# invalid triangle.

while True: # to keep loop looping this code infinitley until user does \

# not input "y" or "Y" for variables yes_no or yes_no_2

    if num_valid == 0 and loop_fixer == 0:

# Above line of code is used to run the code. Both conditions are needed \

# to run first part of loop. The second condition was placed in case the \

# user's first input produces an invalid or degenerate triangle (hence not \ 

# changing the value of the num_valid variable) which will keep the first \ 

# prompt looping despite the fact that the user had already used it. So in \ 

# short, eveything under this if-statement up until variable "yes_no_2" \

# has been defined will only run once, then the program will move on to \

# the next part of the code. 

        yes_no = input("Do you wish to process a triangle (Y or N)?  ")

# above line of code prompts user to continue or not. If user enters "Y" or \

# "y" then the game continue, otherwise a closing message appears and game \

# ends.

        if yes_no == "y" or yes_no == "Y":

            AB = float(input('\nEnter length of side AB: '))

            BC = float(input('\nEnter length of side BC: '))

            CA = float(input('\nEnter length of side CA: '))

# Above 3 lines allow user to input 3 float values for length of 3 sides. 



            if AB + BC < CA or BC + CA < AB or AB + CA < BC:

# above line is condition for shape not to be a triangle.

                print("\n\n  Not a Triangle")

                loop_fixer += 1

# above line is used so that the value of loop_fixer changes so that the \

# the second condition of the if statement is not met so that the second \

# part of the code would run.

                continue

            elif (AB + BC) == CA or (BC + CA) == AB or (CA + AB) == BC:

# above line is condition for if shape is a degenerate triangle.

                print("\n\n  Degenerate Triangle")

                loop_fixer += 1

# above line is used so that the value of loop_fixer changes so that the \

# the second condition of the if statement is not met so that the second \

# part of the code would run.

                continue

            else:

# The above else statement is used if the 3 inputs provided by the user \

# output a valid triangle.



                a_rad = math.acos((BC**2 + CA**2 - AB**2) / (2 * BC * CA))

                b_rad = math.acos((AB**2 + CA**2 - BC**2) / (2 * AB * CA))

                c_rad = math.acos((AB**2 + BC**2 - CA**2) / (2 * AB * BC))

# above 3 lines are the equations used to find the three \

# different angles formed by the triangle using the input \

# lengths provided by user, and using cosine inverse \ 

#function.                  



                a_deg = a_rad * 180 / math.pi

                b_deg = b_rad * 180 / math.pi

                c_deg = c_rad * 180 / math.pi

# above 3 lines convert the three angles found in radians to degrees, by \

# multiplying value for angle in radian by (180 / pi)



                a_deg = round(a_deg, 1)

                b_deg = round(b_deg, 1)

                c_deg = round(c_deg, 1)

                a_rad = round(a_rad, 1)

                b_rad = round(b_rad, 1)

                c_rad = round(c_rad, 1)

# above 6 lines of code round answers to one decimal point.             



                perimeter = AB + BC + CA



                perimeter = round(perimeter, 1)

# above line rounds value for perimeter to one decimal place.   

                area = 0.25 * (math.sqrt( (AB + BC - CA) * (AB - BC + CA) * (BC + CA - AB) * (AB + BC + CA) ))

# above line is the variable "area" and it is used to find the area of \ 

# the triangle by using Heron's Formula by utilizing the 3 user \

# inputs for length.                

                area = round(area, 1)

# above line rounds value for area to one decimal place.

                if (AB + BC) > CA or (AB + CA) > BC or (CA + BC) > AB:

                    num_valid += 1

# The above 2 lines ensure that the triangle with lengths provided is \

# valid and hence the value for the variable "num_valid" increaces by 1.

                    print("\n\n  Valid Triangle")

                    print("\n  Triangle sides:")

                    print("    Length of side AB:", AB)

                    print("    Length of side BC:", BC)

                    print("    Length of side CA:", CA)

                    print("\n  Degree measure of interior angles:")

                    print("    Angle A:", b_deg)

                    print("    Angle B:", c_deg)

                    print("    Angle C:", a_deg)
# You may notice that for the above 3 print statements, the variables are \
# mixed up; this was done purposefully to solve a bug where the program \
# would mix up between the outputs of the user and enter them in a wrong \
# order.
                    print("\n  Radian measure of interior angles:")

                    print("    Angle A:", b_rad)

                    print("    Angle B:", c_rad)

                    print("    Angle C:", a_rad)
# You may notice that for the above 3 print statements, the variables are \
# mixed up; this was done purposefully to solve a bug where the program \
# would mix up between the outputs of the user and enter them in a wrong \
# order.

                    print("\n  Perimeter and Area of triangle:")

                    print("    Perimeter of triangle:", perimeter)

                    print("    Area of triangle:", area)

                    print("\n  Types of triangle:")

                    if AB != BC and AB != CA and BC != CA:

                        print("    Scalene Triangle")

                    if (AB == BC) or (AB == CA) or (BC == CA):

                        print("    Isosceles Triangle")

                    if AB == BC == CA:

                        print("    Equilateral Triangle")

                    if AB**2 + BC**2 == CA**2 or AB**2 + CA**2 == BC**2 or CA**2 + BC**2 == AB**2:

                        print("    Right Triangle")

                    else:

                        print("    Oblique Triangle")

                    if a_deg > 90 or b_deg > 90 or c_deg > 90:

                        print("    Obtuse Triangle")  


        else:
 
            print("")
 
            print("Number of valid triangles:",num_valid )
 
            break
    print("")    
    

    yes_no_2 = input("Do you wish to process another triangle? (Y or N) ")

# above line of code prompts user to continue or not. If user enters "Y" or \

# "y" then the game continue, otherwise a closing message appears and game \

# ends.

    if yes_no_2 == "y" or yes_no_2 == "Y":

        AB = float(input('\nEnter length of side AB: '))

        BC = float(input('\nEnter length of side BC: '))

        CA = float(input('\nEnter length of side CA: '))

# Above 3 lines allow user to input 3 float values for length of 3 sides. 

        if AB + BC < CA or BC + CA < AB or AB + CA < BC:

# above line is condition for shape not to be a triangle.

                print("\n\n  Not a Triangle")

                continue

        elif (AB + BC) == CA or (BC + CA) == AB or (CA + AB) == BC:

# above line is condition for if shape is a degenerate triangle.

            print("\n\n  Degenerate Triangle")

            continue

        else:



            a_rad = math.acos((BC**2 + CA**2 - AB**2) / (2 * BC * CA))

            b_rad = math.acos((AB**2 + CA**2 - BC**2) / (2 * AB * CA))

            c_rad = math.acos((AB**2 + BC**2 - CA**2) / (2 * AB * BC))

# above 3 lines are the equations used to find the three \

# different angles formed by the triangle using the input \

# lengths provided by user, and using cosine inverse function. 



            a_deg = a_rad * 180 / math.pi

            b_deg = b_rad * 180 / math.pi

            c_deg = c_rad * 180 / math.pi

# above 3 lines convert the three angles found in radians to degrees, by \

# multiplying value for angle in radian by (180 / pi)

            a_deg = round(a_deg, 1)

            b_deg = round(b_deg, 1)

            c_deg = round(c_deg, 1)

# above 6 lines of code round answers to one decimal point.

            a_rad = round(a_rad, 1)

            b_rad = round(b_rad, 1)

            c_rad = round(c_rad, 1)



            perimeter = AB + BC + CA



            perimeter = round(perimeter, 1)

# above line rounds value for perimeter to one decimal place.       

            area = 0.25 * (math.sqrt( (AB + BC - CA) * (AB - BC + CA) * (BC + CA - AB) * (AB + BC + CA) ))

# above line is the variable "area" and it is used to find the area of \ 

# the triangle by using Heron's Formula by utilizing the 3 user \

# inputs for length.              

            area = round(area, 1)

# above line rounds value for area to one decimal place.

            if (AB + BC) > CA or (AB + CA) > BC or (CA + BC) > AB:

                num_valid += 1

# The above 2 lines ensure that the triangle with lengths provided is \

# valid and hence the value for the variable "num_valid" increaces by 1.

                print("\n\n  Valid Triangle")

                print("\n  Triangle sides:")

                print("    Length of side AB:", AB)

                print("    Length of side BC:", BC)

                print("    Length of side CA:", CA)

                print("\n  Degree measure of interior angles:")

                print("    Angle A:", b_deg)

                print("    Angle B:", c_deg)

                print("    Angle C:", a_deg)
# You may notice that for the above 3 print statements, the variables are \
# mixed up; this was done purposefully to solve a bug where the program \
# would mix up between the outputs of the user and enter them in a wrong \
# order.
                print("\n  Radian measure of interior angles:")

                print("    Angle A:", b_rad)

                print("    Angle B:", c_rad)

                print("    Angle C:", a_rad)
# You may notice that for the above 3 print statements, the variables are \
# mixed up; this was done purposefully to solve a bug where the program \
# would mix up between the outputs of the user and enter them in a wrong \
# order.
                print("\n  Perimeter and Area of triangle:")

                print("    Perimeter of triangle:", perimeter)

                print("    Area of triangle:", area)

                print("\n  Types of triangle:")

                if AB != BC and AB != CA and BC != CA:

                    print("    Scalene Triangle")

                if (AB == BC) or (AB == CA) or (BC == CA):

                    print("    Isosceles Triangle")

                if AB == BC == CA:

                    print("    Equilateral Triangle")

                if AB**2 + BC**2 == CA**2 or AB**2 + CA**2 == BC**2 or CA**2 + BC**2 == AB**2:

                    print("    Right Triangle")

                else:

                    print("    Oblique Triangle")

                if a_deg > 90 or b_deg > 90 or c_deg > 90:

                    print("    Obtuse Triangle")

    else:

        print("")

        print("Number of valid triangles:",num_valid )

        break
        
        