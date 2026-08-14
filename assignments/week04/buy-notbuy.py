# โปรแกรมช่วยตัดสินใจเลือกซื้อสินค้าตามงบประมาณรวม

def shopping_decision():
    # สร้าง list ว่างชื่อ prices ไว้รอเก็บราคาสินค้า 6 ชิ้น
    prices = []
    
    #รับราคาสินค้า 6 รายการเก็บใส่ list
    print("Enter prices of 6 items:")

    # วนลูป 6 รอบ (i จะเป็น 1 ถึง 6) รับราคาสินค้าทีละชิ้น
    for i in range(1, 7):
        price = float(input(f"Item {i}: "))
        prices.append(price)
        
    #รับงบประมาณรวม
    budget = float(input("Enter total budget: "))
    
    # สร้างตัวแปรเก็บยอดซื้อสะสม (เริ่มที่ 0) และ list ว่างเก็บราคาสินค้าที่ซื้อได้จริง
    current_total = 0
    bought_items = []
    
    #วนลูปเช็กราคาสินค้าทีละชิ้นตามลำดับ
    for i, price in enumerate(prices, start=1):
        # แปลงราคาเป็นจำนวนเต็มถ้าไม่มีทศนิยม เพื่อความสวยงามตอนปริ้นท์
        display_price = int(price) if price.is_integer() else price
        
        # เช็กเงื่อนไข: (ยอดสะสมเดิม + ราคาสินค้าชิ้นปัจจุบัน) เกินงบที่มีไหม?
        if current_total + price <= budget:
            current_total += price # ถ้างบพอ: เอาราคาชิ้นนี้ไปบวกเพิ่มในยอดสะสม
            bought_items.append(display_price) # เก็บราคานี้ลงใน list สินค้าที่ซื้อได้
            print(f"Item {i}={display_price} -> buy")
        else:
            print(f"Item {i}={display_price} -> cannot buy")

        # แสดงยอดซื้อสะสมปัจจุบัน (ถ้าเป็นเลขลงตัวให้แสดงเป็นจำนวนเต็ม)
        display_total = int(current_total) if current_total.is_integer() else current_total
        print(f"Current total = {display_total}")
        
    # คำนวณงบประมาณที่เหลืออยู่ (งบตั้งต้น - ยอดที่จ่ายไปจริง)
    remaining = budget - current_total
    display_remaining = int(remaining) if remaining.is_integer() else remaining
    
    print(f"Bought items: {bought_items}")
    print(f"Total spent: {display_total}")
    print(f"Remaining budget: {display_remaining}")

if __name__ == "__main__":
    shopping_decision()