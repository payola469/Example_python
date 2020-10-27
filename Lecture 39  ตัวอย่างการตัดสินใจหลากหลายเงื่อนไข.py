InputScore = int(input("กรอกคะแนนที่ได้รับ : "))
if InputScore >= 80:
    print("คุณได้รับเกรด A")
elif InputScore >= 75:
    print("คุณได้รับเกรด B+")
elif InputScore >= 70:
    print("คุณได้รับเกรด B")
elif InputScore >= 65:
    print("คุณได้รับเกรด C+")
elif InputScore >= 60:
    print("คุณได้รับเกรด C")
elif InputScore >= 55:
    print("คุณได้รับเกรด D+")
elif InputScore >= 50:
    print("คุณได้รับเกรด D")
else:
    print("คุณได้รับเกรด F")