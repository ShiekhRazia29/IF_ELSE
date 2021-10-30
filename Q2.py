# Q6 Maximum of three numbers
a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter Third number:"))
if a > b and a > c:
    print(" A is maximum")
elif b > a and b > c:
    print("B is maximum")
else:
    print("C is maximum")