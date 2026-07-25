#แสดงเมนู
print("Select conversion direction : ")
print("1. THB to USD")
print("2. USD to THB")
choice = input("Enter your choice : ") #ทางเลือกที่ผู้ใช้เลือก

#สิ่งที่จารย์กำหนดมา 
# rate: 1 USD  = 35.5 THB

if choice == "1":
    a = float(input("Enter a in THB : ")) #รับค่าเป็นทศนิยม
    b = a / 35.5 #ส่วนในการคำนวณบาทให้เป็นดอลลาร์
    print(f"{a}THB = {b:.2f}USD")

elif choice == "2":
    a = float(input("Enter a in USD : "))
    b = a*35.5 #ส่วนในการคำนวณดอลลาร์ให้เป็นบาท
    print(f"{a}USD = {b:.2f}THB")

#เมื่อพิมพ์นอกเหนือทางเลือก 1 & 2
else :
    print("Invalid choice")
