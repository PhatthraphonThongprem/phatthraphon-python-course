# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal ราคาเต็มเท่าไหร่
subtotal = item_price * quantity

# TODO: Calculate discount amount ได้ส่วนลด
discount = subtotal * (discount_precent / 100)

# TODO: Calculate price after discount ราคาหลังแล้ว
price = subtotal - discount

# TODO: Calculate tax amount ภาษีเท่าไหร่
tax = price * (tax_percent / 100)

# TODO: Calculate final total สรุปต้องจ่ายเท่าไหร่
final_total = price + tax

# TODO: Display itemized receipt พ่นออกมาจากทางหน้าจอ
print ("Subtatal =" , subtotal)
print ("Discount= " , str(discount))
print ("Price after discount =" , price)
print (f"Tax amount = {tax} and final total = {final_total}")