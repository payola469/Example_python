userInput = int(input("Enter Number of Your Favorites Fruits :"))
myFruits = set() #set() แปลว่าค่าว่าง // ถ้าใส่เป็น {} ระบบจะเข้าใจว่าข้อมูลประเภท Dictionary
while(len(myFruits)<userInput):
    myFruits.add(input("Fruits : "))
    print(myFruits)