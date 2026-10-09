"""
เขียนจากบนลงล่าง
2 type pf programming
1. structured programming ==> การเขียนโปรแกรมเชิงโครงสร้าง เช่น ภาษา C, Pascal, Fortran, java, python
2. object-oriented programming ==> การเขียนโปรแกรมเชิงวัตถุ เช่น ภาษา C++, Java, Python
python เป็นภาษาโปรแกรมที่สนับสนุนทั้ง 2 แบบ
- ถ้าเขียนโปรแกรมแบบ structured programming จะเรียกว่า procedural programming
- ถ้าเขียนโปรแกรมแบบ object-oriented programming จะเรียกว่า object-oriented programming

ที่ผ่านมาเเขียนแค่เชิงโครงสร้าง แต่ด้านล่างนี้จะเป็นตัวอย่างเชิงวัตถุ

"""

# เป็นลักษระการเขียนแบบ class ==> เขียนเพื่อแก้ปัญหา เป็นแค่ template, แม่แบบ
class ClassName:
    """Class docstring"""

    # ข้อมูลที่ต้องใช้ในการแก้ปัญหา จะถูกเก็บไว้ใน attribute ของ class ระบุไว้ใน constructor method
    def __init__(self, parameters):
        # Constructor method ==> __init__
        self.attribute = value

    # การกระทำที่สมารถนำข้อมูลนั้นไปแก้ปัญหา เรียกว่า method ของ class
    def method_name(self): # ทุก constructor method ต้องมี self เป็น parameter ตัวแรก
        # Instance method
        return something

    def methods_name2(self):
        pass


# การสร้างวัตถุของ class ==> เอา class มาใช้
myObj = ClassName(parameters)

# ตรงนี้ คือ การใช้งานวัตถุจาก class ที่สร้างขึ้นมา
print(myObj.attribute)
resultFromMethod = myObj.method_name()
myObj.method_name2()

myObj2 = ClassName(parameters)
print(myObj2.attribute)
print(myObj2.method_name())
myObj2.method_name2()
