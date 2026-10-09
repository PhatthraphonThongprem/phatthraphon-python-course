# เป็นตัวอย่างการเขียนที่แก้ปัญหาในเรื่องของรถยนต์ โดยใช้ class เพื่อสร้าง template ของรถยนต์
class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    vehicle_type = "Car"
    
    def __init__(self, brand, model, year): # รถทุกคันต้องมีข้อมูลพื้นฐาน 3 อย่าง คือ ยี่ห้อ, รุ่น, ปีที่ผลิต
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0    # ระยะทางสะสมรวมของรถยนต์
        # self.wheels = 4 ก็ได้ แต่เราไม่ได้ตั้งการให้รถทุกคันเปลี่ยนแปลงจำนวนล้อได้ จึงเขียนเป็นแบบด้านบน คือ เป็น class attribute แทนที่จะเป็น instance attribute

    # รถทุกคันต้องทำ 2 อย่างนี้ได้ คือ ขับได้ และ แสดงข้อมูลของรถยนต์ ดังนั้นต้องมี method drive และ get_info

    # การกรำทำแรก คือ รถต้องขับได้ ดังนั้นต้องมี method drive เพื่ออัพเดทระยะทางสะสมของรถยนต์
    def drive(self, distance):
        """Method to update mileage"""
        self.mileage += distance
        return f"Drove {distance} km. Total mileage: {self.mileage} km"
    
    def get_info(self):
        """Method to get car information"""
        return f"{self.year} {self.brand} {self.model} - Mileage: {self.mileage} km"

    # ค้างไว้เดะมาอธิบายอีกที
    @classmethod
    def get_vehicle_type(cls):
        """Class method to access class attributes"""
        return cls.vehicle_type

# Creating instances
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Accessing class attributes
print(f"All cars have {Car.wheels} wheels")
print(f"Vehicle type: {Car.get_vehicle_type()}")

# Accessing instance attributes
print(car1.get_info())
print(car2.get_info())

# Using methods
print(car1.drive(100))
print(car2.drive(250))

"""
ผลลัพธ์ :
All cars have 4 wheels
Vehicle type: Car
2022 Toyota Camry - Mileage: 0 km
2021 Honda Civic - Mileage: 0 km
Drove 100 km. Total mileage: 100 km
Drove 250 km. Total mileage: 250 km
"""

