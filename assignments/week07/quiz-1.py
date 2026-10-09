"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

from turtle import circle


class Rectangle:
    def __init__(self, length, width):
        self.length = length # ค.ยาวของสี่เหลี่ยม
        self.width = width # ค.กว้าง

    # Method to get the area
    def get_area(self): # หาพื้นที่
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self): # หาความยาวรอบรูป
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

"""
ผลลัพธ์ :
50
30

"""

"""
โจทย์
ขอให้เขียน class cercle โดยกำหนดให้ทำงานคล้ายกับ class rectangle 
พร้อมทำงานตัวอย่าง

"""

class Circle:
    def __init__(self, radius):
        self.radius = radius # รัศมีของวงกลม

    # Method to get the area
    def get_area(self): # หาพื้นที่
        return 3.14 * self.radius ** 2

    # Method to get the circumference
    def get_circumference(self): # หาความยาวรอบวงกลม
        return 2 * 3.14 * self.radius

mycircle = Circle(10)
print(mycircle.get_area())
print(mycircle.get_circumference())

"""
ผลลัพธ์ :
314.0
62.800000000000004

"""