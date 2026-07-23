def kiemtrangaythang(ngay, thang):
    if ngay >= 31 or ngay < 1:
        return False
    if thang >= 12 or thang < 1:
        return False
    if thang in [1,3,5,7,8,10,12]:
        return ngay <= 31
    elif thang in [4,6,9,11]:
        return ngay <= 30
    elif thang == 2:
        return ngay <= 29
    return False
def tim_cung_hoang_dao(ngay, thang):
    """Hàm trả về tên cung hoàng đạo dựa vào ngày tháng hợp lệ"""
    if (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 19):
        return "Bạch Dương"
    elif (thang == 4 and ngay >= 20) or (thang == 5 and ngay <= 20):
        return "Kim Ngưu"
    elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 20):
        return "Song Tử"
    elif (thang == 6 and ngay >= 21) or (thang == 7 and ngay <= 22):
        return "Cự Giải"
    elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
        return "Sư Tử"
    elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
        return "Xử Nữ"
    elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 22):
        return "Thiên Bình"
    elif (thang == 10 and ngay >= 23) or (thang == 11 and ngay <= 21):
        return "Bọ Cạp"
    elif (thang == 11 and ngay >= 22) or (thang == 12 and ngay <= 21):
        return "Nhân Mã"
    elif (thang == 12 and ngay >= 22) or (thang == 1 and ngay <= 19):
        return "Ma Kết"
    elif (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
        return "Bảo Bình"
    elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
        return "Song Ngư"

chuoi_nhap = input("Input: ").split() 
ngay = int(chuoi_nhap[1].replace(",", ""))
thang = int(chuoi_nhap[3])
if not kiemtrangaythang(ngay, thang):
    print("Output: Ngày hoặc tháng không hợp lệ")
else:
    cung = tim_cung_hoang_dao(ngay, thang)
    print(f"Output: {cung}")