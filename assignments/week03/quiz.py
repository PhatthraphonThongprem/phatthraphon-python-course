# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child // เด็ก
# 13-19: Teenager  //วัยรุ่น
# 20-59: Adult //วัยทำงาน
# 60+: Senior //วัยชรา

# Your code here:
if age > 0 and age <= 12:
    print ("Child")
elif age >= 13 and age <= 19 :
    print ("Teenager")
elif age >= 20 and age <= 59 :
    print ("Adult")
else :
    print ("Senior")

# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin: # โปรแกรมที่เขียนลงไปทั้งหมดจะอยู่ใน if นี้เสมอ
    print("PIN accepted")
    while True: # โปแกรมนี้ต้องทำเป็น loop
        print("\n1. Check Balance")
        print("2. Withdraw") #ถอนเงิน
        print("3. Deposit") #ฝากเงิน
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1." :
            print("Balance", balance, "บาท")
        elif choice == "2." :
            withdraw = flaot(input("Amount : "))
            balance = balance - withdraw
        elif choice == "3." :
            deposit = flaot(input("Amount : "))
            balance = balance + deposit
        else choice == "4.":
            break 
else:
    print("Invalid PIN")
