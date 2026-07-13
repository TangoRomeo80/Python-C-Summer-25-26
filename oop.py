# This file contains class object related codes
# class Animal:
#     def make_sound(self):
#         print("Gheu")

# a = Animal()
# a.make_sound()

# Class example in Java
# class Car{
#     private String model;
#     private String color;
#     private int doors;
#     private String engineType;
#     private double displacement;

#     Car(String model, String color, int doors, String engineType, double displacement) {
#         this.model = model;
#         this.color = color;
#         this.doors = doors;
#         this.engineType = engineType;
#         this.displacement = displacement;
#     }
# }

# class ToyotaCar{
#     public static string manufacturer = "Toyota";
# }

# class ToyotaCar:
#     # Static variable
#     manufacturer: str = "Toyota"
#     # Car has: Model, Color, Doors, Engine Type, displacement
#     # Constructor
#     def __init__(self, model: str, color: str, doors: int, engine_type: str, displacement: float):
#         # Instance variables
#         self.model = model
#         self.color = color
#         self.doors = doors
#         self.engine_type = engine_type
#         self.displacement = displacement
    
#     # Instance method
#     # Instance methods always take self (similar to "this") as the first parameter. Self points to the current object. 
#     # It is used to access variables that belongs to the specific object of the class.
#     def display_info(self):
#         print(f"Manufacturer: {ToyotaCar.manufacturer}")
#         print(f"Model: {self.model}")
#         print(f"Color: {self.color}")
#         print(f"Doors: {self.doors}")
#         print(f"Engine Type: {self.engine_type}")
#         print(f"Displacement: {self.displacement}L")
    
#     # We use class methods to modify class state/variables that apply across all instances of the class. 
#     # Class methods take cls as the first parameter while instance methods take self.
#     # Class methods also uses the @classmethod decorator to flag it as a class method.
#     @classmethod
#     def change_manufacturer(cls, new_manufacturer: str):
#         cls.manufacturer = new_manufacturer

# # Toyota Premio is a car
# premio = ToyotaCar("Premio", "Silver", 4, "Petrol", 2.0)
# premio.display_info()
# print()
# ToyotaCar.change_manufacturer("Toyota Motors")
# premio.display_info()
# print()

# # Toyota Supra is also a car
# supra = ToyotaCar("Supra", "Red", 2, "Petrol", 3.0)
# supra.display_info()

# Encapsulation means restricting external access without any control
# In java, default access modifier is private, which means it is only accessible in the same class.
# In python, default access modifier is public, which means it is accessible from anywhere.
# class Car:
#     def __init__(self, model: str, color: str, doors: int, engine_type: str, displacement: float):
#         # __ means private access modifier, which means it is only accessible in the same class.
#         # _ means protected access modifier, which means it is accessible in the same class and subclasses.
#         self.__model = model
#         self.__color = color
#         self.__doors = doors
#         self.__engine_type = engine_type
#         self.__displacement = displacement

#     # We implement getter and setter methods to access private variables from outside the class. 
#     # This ensure abstraction and encapsulation of the class by hiding the internal implementation details and restricting direct access.
#     def get_model(self):
#         return self.__model

#     def set_model(self, model: str):
#         self.__model = model

#     def get_color(self):
#         return self.__color

#     def set_color(self, color: str):
#         self.__color = color

#     def get_doors(self):
#         return self.__doors

#     def set_doors(self, doors: int):
#         self.__doors = doors

#     def get_engine_type(self):
#         return self.__engine_type

#     def set_engine_type(self, engine_type: str):
#         self.__engine_type = engine_type

#     def get_displacement(self):
#         return self.__displacement

#     def set_displacement(self, displacement: float):
#         self.__displacement = displacement

# c1 = Car("Premio", "Silver", 4, "Petrol", 2.0)
# print(f"Model: {c1.get_model()}")
# print(f"Color: {c1.get_color()}")
# print(f"Doors: {c1.get_doors()}")
# print(f"Engine Type: {c1.get_engine_type()}")
# print(f"Displacement: {c1.get_displacement()}L")
# print(c1.__model) # Invalid

