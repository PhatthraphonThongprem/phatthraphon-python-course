"""
โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
-   ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
-   ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise ValueError
-   ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisionError
-   โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย finally

ตัวอย่างผลลัพธ์ที่คาดหวัง

ตัวเลขที่ 1: 10
ตัวเลขที่ 2: 0
เครื่องหมาย (+, -, *, /): /

ไม่สามารถหารด้วยศูนย์ได้
จบการทำงาน
"""

try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")
    result = 0

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น +, -, *, / เท่านั้น")

    print(f"{num1} {operator} {num2} = {result}")

except ValueError as e:
    # ดักจับทั้งการใส่ตัวเลขผิด และการใส่เครื่องหมายผิด
    if "เครื่องหมายต้องเป็น" in str(e):
        print(e)
    else:
        print("กรุณากรอกข้อมูลที่เป็นตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

except Exception as e:
    print("ทำอะไรไม่ได้บางอย่างแต่ไม่แน่ใจว่าคืออะไร")

finally:
    print("จบการทำงาน")