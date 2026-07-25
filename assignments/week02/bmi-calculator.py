#รับค่า
height = float(input("Enter your height (m) : ")) #นน.
weight = float(input("Enter your weight (kg) : ")) #ส่วนสูง

#ส่วนคำนวณ
bmi = weight / (height ** 2)
print(f"Your BMI is : {bmi:.2f}") #แสดงผลลัพธ์

if bmi < 18.5 :
    print("Underweight") #นน.น้อยกว่าเกณฑ์
elif bmi <= 24.9 :
    print("Normal weight") #ปกติ/สุขภาพดี
elif bmi <= 29.9 :
    print("Overweight") #เกินเกณฑ์
else :
    print("Obese") #อ้วน
