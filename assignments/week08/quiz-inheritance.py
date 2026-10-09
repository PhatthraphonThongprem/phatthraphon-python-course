""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle :
    def __init__(self, brand, model, year) :
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle info :\nBrand : {self.brand},\n Model:{self.model},\n Year : {self.year}"

class Car (Vehicle) :

    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Car info :\n Brand : {self.brand},\n Model: {self.model},\n Year :{self.year},\n Number of Doors : {self.number_of_doors}"

car1 = Car("Honda", "Civic", "2021", "4")
print(car1.get_info())

car2 = Vehicle("Toyota", "Camry", "2022")
print(car2.get_info())