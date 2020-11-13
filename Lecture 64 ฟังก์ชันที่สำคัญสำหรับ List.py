myFriends = ["Alice", "Bob", "Trudy"] # list กำหนดมา 3 คน
myFriends.append("Prame") # .append คือการเพิ่ม list มา 1 รายการ คือ Prame
print(myFriends) # ตอนนี้จะมี ['Alice', 'Bob', 'Trudy', 'Prame']
myFriends.remove("Bob") # .remove คือทำการลบ ชื่อ Bob (อันนี้ในกรณีรู้ชื่อ)
print(myFriends) # ตอนนี้จะมี ['Alice', 'Trudy', 'Prame']
myFriends[2] = 'Pramey' # ทำการแก้ไขชื่อ(หรือที่เรียกว่าแทนค่า) ลำดับที่ 2 (0,1,2) คือ Prame ให้เปลี่ยนเป็น Pramey
print(myFriends) # ตอนนี้จะมี ['Alice', 'Trudy', 'Pramey']


# ในกรณจะลบแต่ไม่รู้ว่าชื่ออะไรเราสามารถแทนด้วยตำแหน่งดังนี้
del myFriends[0] # ลบตำแหน่งที่ 0 ออก
print(myFriends) # จะเหลือ ['Trudy', 'Pramey']