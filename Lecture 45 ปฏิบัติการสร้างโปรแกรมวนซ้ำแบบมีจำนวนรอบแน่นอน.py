InputRound = int(input("Round : "))
sum = 0
for x in range(InputRound):
    InputNumber = int(input("x"+str(x+1)+" : "))
    sum += InputNumber
print("ผลลัพธ์ : ", sum)