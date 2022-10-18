#############################################################################
# Project 1
# Author:  Zaid Qourah
# Date:    9/12/2022
# Purpose: This program converts rods to other distances. \
# This program also calculates time in minutes needed to \ 
# walk a certain distance. 
#############################################################################

# Line 11 prompts the user to input a value for distance in Rods
rods_str = input('Input rods: \n')
# Line 14 converts the string "rods_str" to \ 
# a floating point value to help python carry out calculations
rods_str = float(rods_str)
# Line 16 equates meters to rods
Meters = float(rods_str * 5.0292)
# Line 19 shows the variable "rod_to_feet" \ 
# which is necessary to calculate distance in feet
rod_to_feet = float(5.0292 / 0.3048)
# Line 22 equates feet to rods \
# using variables "rods_str" and "rod_to_feet"
Feet = float(rods_str * rod_to_feet)
# Line 25 shows the variable "rod_to_mile" \
# This is necessary to calculate distance in miles
rod_to_mile = float(1609.34 / 5.0292)
# Line 27 equates miles to rods using variables "rods_str" and "rod_to_mile"
Miles = float(rods_str / rod_to_mile)
# Line 29 equates furlongs to rods using the variable "rods_str"
Furlongs = float(rods_str / 40)
# Line 32 shows conversion of speed in miles/hour to rods/minute \
# with average walking speed of 3.1 miles/hour
speed_in_rods_in_minutes = float((3.1 / 60) * rod_to_mile)
# Line 35 calculates the time needed to \ 
# walk the distance inputed by the user in rods and minutes
minutes_rods = float(rods_str / speed_in_rods_in_minutes)
# Line 37 rounds the answer from line 28 to three decimal places
minutes_rods = round(minutes_rods, 3)

print("You input ", end = "")

print( rods_str, end = "")

print(" rods.")

print()

print("Conversions")

print("Meters:", round(Meters, 3))

print("Feet:", round(Feet, 3))

print("Miles:", round(Miles, 3))

print("Furlongs:", round(Furlongs, 3))

print("Minutes to walk", rods_str, end = "")

print(" rods: ", end = "")

print(minutes_rods)