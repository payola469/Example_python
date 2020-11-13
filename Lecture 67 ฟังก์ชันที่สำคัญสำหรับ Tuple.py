tupleEx = (1, 2, 199, 4, 5) #ไม่สามารถแก้ไข เพิ่ม และ ลบ ได้
listEx = [10, 20, 1990, 40, 50] #สามารถแก้ไข เพิ่ม และ ลบ ได้
print(len(tupleEx)) # แสดงค่าต่ำสุด
print(max(tupleEx)) # แสดงค่าสูงสุด
print(tuple(listEx)) # แปลง listEx ให้เป็น tuple

# ข้อสังเกต tuple จะเป็น () // list จะเป็น []