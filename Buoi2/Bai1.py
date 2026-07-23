a = str(input("Nhap thang nam : ")).split()
def tinhnamnhuan(nam):
    if nam % 100 == 0:
        if nam % 400 == 0:
            return True
        else:
            return False
    elif nam % 4 == 0:
        return True
    else:
        return False
nam = a[3]
thang= a[1].replace(",", "")
if int(thang) == 2:
    if tinhnamnhuan(int(nam)) :
        print(29)
    else:
        print (28)
elif int(thang) in [1,3,5,7,8,10,12]:
    print (31)
elif int(thang) in [4,6,9,11]:
    print(30)