#############################################################################
# Project 11
#
# This program will create a class called "Volume" where it will contain an \
# object that stores magnitude of volume and units of meausrments. For this \
# class, multiple built-in methods will be created for it which are: \
#__init__ , __str__ , __repr__ , is_valid , get_units ,get_magnitude, metric\
# customary , __eq__ , add , sub. These built in methods will be described \
# in depth in dcostrings under each method for clarity and consicness. These 
# built-in methods can be used to manipulate data and can be implemented in\
# functions and other programs.
#############################################################################

import copy # used to create shallow copy of certain objects

UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude = 0, units = "ml"):
        """
        This method initializes the parameters of an object which is an\
        instance of the class. The self parameter is used conventially\
        The magintude parameter is initilaized to zero and the units\
        parameter.
        """
        self.__magnitude = magnitude # initialize variable
        self.__units = units # initialize variable
        
        if self.__units in UNITS: #. valid unit
            pass
        else: #. invalid unit
            self.__units = None
            self.__magnitude = None


        if self.__magnitude != None: #. possibly valid magnitude
            
            try:
                self.__magnitude = float(self.__magnitude)
                
            except: #if magnitude is invalid
                self.__magnitude = 0
                self.__units = None
                
            if self.__magnitude < 0: #if magnitude value less than 0
                self.__magnitude = 0
                self.__units = None
                

        
    def __str__(self):    
        """
        This method takes the object "self" as the parameter and this method
        returns a string representation of the object and magnitude rounded to
        to 3 decimal places.
        """
        if self.__units != None:
            out_string = "{:.3f} {}".format(self.__magnitude, self.__units)
            return out_string
        else:
            return("Not a Volume")
        
    def __repr__(self):   
        """
        This method takes the object "self" as the parameter and this method
        returns a string representation of the object and magnitude rounded to
        to 3 decimal places.
        """
        if self.__units != None:
            out_string = "{:.6f} {}".format(self.__magnitude, self.__units)
            return out_string
        else:
            return("Not a Volume")
        
    def is_valid(self):    
        """
        This method takes the object/instance of the class "self" as a parameter
        and checks wheather the object qualifies as a valid volume. This is the
        case when units are ml or oz and  magnitude > 0.
        """
        if self.__units != None:
            return True
        else:
            return False
    
    def get_units(self):    
        """
        This method takes the object/instance of the class "self" as a parameter
        and returns units, if no valid one exists then return None.
        """
        return self.__units
    
    def get_magnitude(self):
        """
        This method takes the object/instance of the class "self" as a parameter
        and returns magnitude, if no valid one exists then return None.
        """
        return self.__magnitude
    
    def metric(self):
        """
        This method takes the object/instance of the class "self" as a parameter
        and checks if the units is in metric system, if it is the object
        is returned. If not then a shallow copy of the object was created as to
        not to alter the current object, and then both magnitude and units
        attributes of objects will be converted to metric system.
        """
        metric_vol = copy.copy(self) # create shallow copy, so that any changes
        # made to this object does not affect the original object.
        
        if metric_vol.__units == "ml":
            return self
        
        if metric_vol.__units == "oz":
            metric_vol.__magnitude = metric_vol.__magnitude * MLperOZ
            metric_vol.__units = "ml"
            return metric_vol
        
        else: # This will return "Not a Volume"
            return metric_vol

        
    def customary(self):  
        """
        This method takes the object/instance of the class "self" as a parameter
        and checks if the units is in customary system, if it is the object
        is returned. If not then a shallow copy of the object was created as to
        not to alter the current object, and then both magnitude and units
        attributes of objects will be converted to customary system.
        """
        customary_vol = copy.copy(self) # create shallow copy, so that any
        #changes made to this object does not affect the original object.
        
        if customary_vol.__units == "ml":
            customary_vol.__magnitude = customary_vol.__magnitude / MLperOZ
            customary_vol.__units = "oz"
            return customary_vol
        
        if customary_vol.__units == "oz": 
            return self
        
        else: # This will return "Not a Volume"
            return customary_vol
        
    def __eq__(self, other): 
        """
        This method takes the object/instance of the class "self" as a parameter
        and also another object of the same class which is a parameter "other".
        This method compares the two objects and tests wheather they are 
        equivilant or not.
        """
        self_copy = copy.copy(self) # makes shallow copy so original object is 
        # not affected.
        if self.__units == other.__units:
            if abs(self.__magnitude - other.__magnitude) <= DELTA:
                return True
            else:
                False
        else: #if the units attribute of each object is not equal to the other.
            if self.__magnitude == other.__magnitude: # same magnitude but different
            #unit always returns False.
                return False
            else:
                if self_copy.__units == "ml":
                    self_copy.__magnitude = self_copy.__magnitude / MLperOZ
                    self_copy.__units = "oz"
                    # the above three lines convert an object from ml to oz as 
                    # well as all of its attributes.

                elif self_copy.__units == "oz":
                    self_copy.__magnitude = self_copy.__magnitude * MLperOZ
                    self_copy.__units = "ml"
                    # the above three lines convert an object from ml to oz as 
                    # well as all of its attributes.
        if abs(self_copy.__magnitude - other.__magnitude) == DELTA:
            return True
        else:
            return False 

    
    def add(self,other):
        """
        This method takes the object/instance of the class "self" as a parameter
        and also another object of the same class which is a parameter "other".
        This method adds the object other to the object self. In example, if 
        both objects are of type Volume, the units have to be made same so that
        magnitudes can be added. In case that a constant is added with no unit,
        it will be added normally to the magnitude. 
        """
        self_copy = copy.copy(self) # makes shallow copy of object so that the
        # original will remain unchanged.
        if type(other) == float or type(other) == int:
            self_copy.__magnitude += other
            return self_copy
        # the above if-statement and its conditions are executed if addition
        # is occuring with a constant.
        item = Volume(object) # constructs new object that can be altered.
        item.__units = self.__units # units for new object are based on units for
        # "self" object.
        if item.__units == "ml":
            item.__magnitude = (other.__magnitude * MLperOZ) + self.__magnitude
        elif item.__units == "oz": 
            item.__magnitude = (other.__magnitude / MLperOZ) + self.__magnitude
        return item

    def sub(self,other):
        """
        This method takes the object/instance of the class "self" as a parameter
        and also another object of the same class which is a parameter "other".
        This method subtracts the object other to the object self. In example,
        if both objects are of type Volume, the units have to be made same so
        that magnitudes can be subtracted. In case the constant is minused with
        no unit, it will be removed normally to the magnitude. 
        """
        self_copy = copy.copy(self) # makes shallow copy of object so that the
        # original will remain unchanged.

        if type(other) == float or type(other) == int:
            self_copy.__magnitude -= other
            return self_copy
        # the above if-statement and its conditions are executed if addition
        # is occuring with a constant.
        item = Volume(object) # constructs new object that can be altered.
        item.__units = self.__units # units for new object are based on units 
        if item.__units == "ml":
            item.__magnitude = (other.__magnitude * MLperOZ * -1) + self.__magnitude
        elif item.__units == "oz": 
            item.__magnitude = (other.__magnitude / MLperOZ * -1) + self.__magnitude
        if item.__magnitude < 0:
           item.__magnitude = 0
           item.__units = None
        # the above if-statement deals with an invalid float magnitude.
        return item



