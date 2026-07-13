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

