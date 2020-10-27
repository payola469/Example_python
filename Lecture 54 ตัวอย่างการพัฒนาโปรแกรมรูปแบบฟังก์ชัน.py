def login():
    idinput = input("ID : ")
    passinput = input("Password : ")
    if idinput == "1234" and passinput == "1234":
        print("รหัสผ่านถูกต้อง")
        print("v")
        print("v")
        ShowMenu()
    else:
        print("ใส่รหัสผ่านผิด")
        print("v")
        print("v")
        login()
def ShowMenu():
    print("------ Menu ------")
    print("1.คำนวณภาษี ")
    print("2.เครื่องคิดเลข ")
    userselect = input("กรุณาเลือกรายการ : ")
    if userselect == "1":
        VatCalculate()
    elif userselect == "2":
        PriceCalculate()
    else:
        ShowMenu()
def VatCalculate():
    print("")
    print("--- คำนวณภาษี ---")
    price = int(input("กรุณาใส่ราคา : "))
    vat = 7
    ResultVat = price+(price*vat/100)
    print("ราคารวมภาษี :",ResultVat,"บาท")
def PriceCalculate():
    print("")
    print("--- เครื่องคิดเลข ---")
    price1 = int(input("สินค้าราคาชิ้นที่ 1 : "))
    price2 = int(input("สินค้าราคาชิ้นที่ 2 : "))
    print("รวมราคาสินค้า :",price1+price2,"บาท")
ShowMenu()