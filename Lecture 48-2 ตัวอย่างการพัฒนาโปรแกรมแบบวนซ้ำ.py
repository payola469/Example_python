userinput = int(input("number : "))
for x in range(userinput): # จะทำงานตามรอบที่ userinput เข้าไป
    text = ""  # กำหนด text เปล่าๆ
    for y in range(x+1):  # รอบ1 x มีค่าเท่ากับ 0 และ บวก 1 เลยเป็น 1 // รอบ2 x มีค่าเท่ากับ 1 และ บวก 1 เลยเป็น 2
        text += "*"   # แสดง * ตามจำนวนรอบ y => รอบ1 แสดง 1 // รอบ2 แสดง 2
    print(text)

# input 3
# *
# **
# ***

