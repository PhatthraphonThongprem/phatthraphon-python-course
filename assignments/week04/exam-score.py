 #โปรแกรมตรวจผลสอบนักเรียน 5 คน

def check_exam_scores():
    # สร้าง list ว่างไว้เก็บคะแนนนักเรียน 5 คน
    scores = []
    
    # วนลูปรับค่าคะแนนจากผู้ใช้ 5 รอบ
    for i in range(1, 6):
        score = float(input(f"Score of student {i}: "))
        scores.append(score) # เอาคะแนนที่พิมพ์เข้ามาใส่ใน list ที่ชื่อ scores
        
    # วนลูปเพื่อตรวจคะแนนทีละคนตามลำดับใน list scores
    # enumerate ช่วยดึงลำดับ (i เริ่มที่ 1) & ค่าคะแนน (score) ออกมาพร้อมกัน
    for i, score in enumerate(scores, start=1):
        # ถ้าคะแนน50 ขึ้นไปคือผ่าน
        if score >= 50:
            result = "ผ่าน"
        else: #ถ้าน้อยกว่า50 คือไม่ผ่าน
            result = "ไม่ผ่าน"
        
        # ปรับการแสดงผล ถ้าเป็นเลขลงตัว (เช่น 45.0) ให้แสดงเป็น 45
        display_score = int(score) if score.is_integer() else score
        print(f"Student {i}: {display_score} -> {result}")

# ส่วนบรรทัดนี้ไว้สั่งให้ฟังก์ชั่นทำงาน เมื่อเรารันไฟล์นี้โดยตรง
if __name__ == "__main__":
    check_exam_scores()