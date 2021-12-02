import math
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
delta = b**2 - 4*a*c
if delta<0:
    print("Chuong trinh vo nghiem")
elif delta==0:
    print("Chuong trinh co 1 nghiem: ", -b/2*a)
else:
    print("Chuong trinh co 2 nghiem: ")
    print("x1 = ", (-b+math.sqrt(delta))/2*a)
    print("x2 = ", (-b-math.sqrt(delta))/2*a)