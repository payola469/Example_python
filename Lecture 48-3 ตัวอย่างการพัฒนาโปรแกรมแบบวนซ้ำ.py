userinput = int(input("number : "))
for x in range(userinput):
    print("*"*(x+1))   # ตัว * คูณด้วย (x+1) ตัว x มีค่าตามจำนวนรอบของ userinput
    # เช่น รอบ1 จะได้ ("*"*(0+1)) => *
    # เช่น รอบ2 จะได้ ("*"*(1+1)) => **
    # เช่น รอบ3 จะได้ ("*"*(2+1)) => ***

# ย่อจาก 48-2