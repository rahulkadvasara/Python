# # class and objects
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size

# my_tesla=ElectricCar("Tesla","Model S","85kWh")
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())    

# # my_car=Car("Toyota","Corolla")
# # print(my_car.brand)
# # print(my_car.model)
# # print(my_car.full_name())

# # Encaptulation
# class Car:
#     def __init__(self,brand):
#         self.__brand=brand
    
#     def get_brand(self):
#         return self.__brand+" !"
    
# my_tesla = Car("Tesla")

# print(my_tesla.get_brand())

# # Polymorphism
# class Car:
#     # class variables
#     total = 0
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.__model=model
#         # self.total+=1
#         Car.total+=1
#     def get_brand(self):
#         return self.__brand+" !"
#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
#     def fuel_type(self):
#         return "Petrol or Diesel"
#     # static method
#     @staticmethod # -->decorator
#     def general_description():
#         return "Cars are means of transport"
    
#     # decorators to model read only mode
#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#     def fuel_type(self):
#         return "Electric charge"
    
# # tesla=ElectricCar("Tesla","Model S","85kWh")
# # print(isinstance(tesla,Car))
# # print(isinstance(tesla,ElectricCar))

# # my_car = Car("Tata","Safari")
# # print(my_car.model)
# # print(Car.general_description())
# # print(tesla.fuel_type())
# # safari = Car("Tata","Safari")
# # print(safari.fuel_type())
# # print(Car.total)

# # multiple inheritance
# class Battery:
#     def battery_info(self):
#         return "This is Battery"
# class Engine:
#     def engine_info(self):
#         return "This is Engine"
# class Electric(Battery,Engine,Car):
#     pass
# new_tesla = Electric("Tesla","Model S")
# print(new_tesla.engine_info())
# print(new_tesla.battery_info())
