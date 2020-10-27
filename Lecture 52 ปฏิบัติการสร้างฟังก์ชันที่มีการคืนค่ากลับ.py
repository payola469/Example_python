def say(): # ปรกาศฟังชั่น "sayhello"
    print("Hello World!!")  # ในฟังชั่นนี้จะแสดงผลว่า Hello World!!

def SayHello(name):
    return "Hello " + name # return คือการรับค่า จากคำสั่งคือ Hello และ ตามด้วยชื่อ
    print("Hi " + name) #Tips: การ return จะเป็นการจบการทำงานของฟังก์ชัน หมายความว่าโค้ดในฟังก์ชันที่อยู่บรรทัดหลังจาก return จะไม่ทำงานนั่นเอง
    print("Hoho") #Tips: การ return จะเป็นการจบการทำงานของฟังก์ชัน หมายความว่าโค้ดในฟังก์ชันที่อยู่บรรทัดหลังจาก return จะไม่ทำงานนั่นเอง
print(SayHello("jojo")) #ให้แสดงฟังชั่น SayHello และ name = jojo