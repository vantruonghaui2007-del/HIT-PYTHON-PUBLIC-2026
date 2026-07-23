from math import sqrt
a= int(input("Input: "))
b=str(a)
tong=0
def kiemtrasonguyento(a):
    for i in range (2, int(sqrt(a))+1):
        if a % i == 0:
            return False
        return True
for i in range (len(b)):
    tong += int(b[i])
if kiemtrasonguyento(a):
    print(f"So chu so: {len(b)}, Tong: {tong}, {a} la so nguyen to")
else:
    print(f"So chu so: {len(b)}, Tong: {tong}, {a} khong la so nguyen to")