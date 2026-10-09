# ERROR (bugs)
# 3 types => syntax errors / runtime error / logic error
#บริหารความเสี่ยงใน 3 types

age = int(input("Insert you age: ")) # --> runtime error 
print(age)

#ValueError Exception
try:
    age = int(input("กรอกอายุ:"))
    print(f"ปีหน้าคุณจะอายุ {age + 1} ปี")
except ValueError: # ทำหน้าที่ดักจับค่า error
    print("กรุณากรอกอายุเป็นจำนวนตัวเลขจำนวนเต็ม เช่น 20")
    
#ZeroDivisionException
try:
    numertor = float(input("กรอกตัวตั้ง: "))
    denominator = float(input("กรอกตัวหาร: "))
    
    result = numertor / denominator
    print(f"ผลลัพธ์ = {result}")

except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")
    
except ZeroDivisionError: 
    print("ไม่สามารถหารด้วยศูนย์ได้")
    
#FileNotFoundException, PermissionException
try:
    filename = input("ชื่อไฟล์: ")
    
    with open(filename, "r", encoding="uf-8") as file:
        content = file.read()
        
    print("เนื้อหาในไฟล์")
    print(content)

except FileNotFoundError: #ไม่มีไฟล์นี้อยู่จริง
    print(f"ไม่พบไฟล์ชื่อ {filename}")
    
except PermissionError: #สิทธิ์เข้าถึงไฟล์
    print("ไม่มีสิทธิ์เข้าถึงไฟล์นี้")
    
# raise ใช้สำหรับ สั่งให้ python สร้าง exception ขึ้นเอง เมื่อข้อมูลหรือสถานการณ์ไม่เป็นไปตามที่ต้องการ
# แม้คำสั่งจะนั้นจะไม่ผิดไวยากรณ์และ python ยังทำงานต่อไปได้

try:
    score = float(input("กรอกคะแนน 0-100: "))
    
    if not 0 <= score <= 100: # python only
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")
    
except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")

else:
    print(f"บันทึกคะแนน {score} เรียบร้อย")
    
finally: #อย่างเป็นลำดับสุดท้าย
    print("จบการตรวจสอบคะแนน")