start = int(input("Start: "))
step = int(input("Step: "))
result = str("")
for i in range(5):
    result += str(start + step * i + 1)
    print(result)

#รอบที่ 0 :: (1 + (2*0)+1) = 2
#รอบที่ 1 :: (1 + (2*1)+1) = 4
#รอบที่ 2 :: (1 + (2*2)+1) = 6
#รอบที่ 3 :: (1 + (2*3)+1) = 8
#รอบที่ 4 :: (1 + (2*4)+1) = 10
#เพราะฉะนั้นต้องเป็น 2 4 6 8 10