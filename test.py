t = -3
while t > 0:
    x = str(input("nhập chuỗi x: "))
    a = len(x)
    b = True

    if a % 2 ==0:
        for i in range(0, a//2, 1):
            if x[i] != x[a-1-i]:
                b=False
                break
    else:
        print("không đối xứng")

    if b:
        print("Đây là chuỗi đối xứng")
    else:
        print("Không đối xứng")

    t = int(input("Nhập số t: "))

