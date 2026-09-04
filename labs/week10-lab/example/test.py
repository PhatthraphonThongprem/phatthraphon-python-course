# ข้อ 1.
# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3. แสดงผลจำนวนของอักขระในข้อความ text

# ตัวอย่าง
# Insert your text : Boonchoo Jitnipong
# Charecter to find : o
# 5 letter 'o' found in 'Boonchoo Jitnipong' 

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text : ")
char = input("Charecter to find : ")
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

# ข้อ 2.
# เขียนโปรแกรมตรวจสอบความแข็งแรงของ Password
# นิยามของ string password คือ ยาวมากกว่า 8 ตัว , มีตัวอักษร @ 1 ตัว ,มีตัวเลข ,มีตัวอักษร
#
# ตัวอย่างหน้าจอ
# Insert your password : Boonchoo
# Your password is not strong!
#
# Insert your password : Test@123
# Your password is strong!
Password = input("Insert your password :")
lenght = len(password)
words = password.split('@')

if len(word) > 1 and password.count('@') == 1 :
    left = words[0].isalnum()
    right = words[1].isalnum()

else :
    left = False;
    right = False ;

if lenght >= 8 and len(words) == 2 and left and right :
    print("Your password is strong!")

else:
    print("Your password is not strong!")

