# ตัวอย่างการแก้ปัญกาที่เกี่ยวของกับนักเรียน ที่ต้องมีการเก็บข้อมูล เช่น ชื่อ, อายุ, รหัสนักเรียน และรายวิชาที่ลงทะเบียนเรียน
# โดยใช้ class เพื่อสร้าง template ของนักเรียน
class Student:
    """A simple Student class"""
    
    def __init__(self, name, age, student_id):
        self.name = name           # Instance attribute
        self.age = age            # Instance attribute
        self.student_id = student_id  # Instance attribute
        self.courses = []         # Instance attribute (list)
        # courses = [] ==> เป็น course 0 วิชา หรือก็คือ ยังไม่ได้ลงทะเบียนเรียนวิชาไรเลย

    def introduce(self):
        """Method to introduce the student"""
        return f"Hi, I'm {self.name}, {self.age} years old, ID: {self.student_id}"
    
    def add_course(self, course):
        """Method to add a course"""
        self.courses.append(course)
        return f"{course} added successfully!"
    
    def show_courses(self):
        """Method to display all courses"""
        if self.courses:
            return f"Courses: {', '.join(self.courses)}"
        else:
            return "No courses enrolled yet."

# Creating objects (instances)
student1 = Student("Alice", 20, "S001")
student2 = Student("Bob", 19, "S002")

# ตัวอย่างการใช้งาน
# Using methods
print(student1.introduce())
print(student1.add_course("Python Programming"))
print(student1.add_course("Data Structures"))
print(student1.show_courses())

"""
ผลลัพธ์ :
Hi, I'm Alice, 20 years old, ID: S001
Python Programming added successfully!
Data Structures added successfully!
Courses: Python Programming, Data Structures

"""

# สมมุติ
print(student2.introduce())
print(student2.add_course("Mathematics"))
print(student2.show_courses())

"""
ผลลัพธ์ :
Hi, I'm Bob, 19 years old, ID: S002
Mathematics added successfully!
Courses: Mathematics

"""