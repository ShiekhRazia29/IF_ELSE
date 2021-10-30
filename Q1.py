# A number divisible by 11 and 5
num1 = int(input("Enter a number:"))
if num1 % 5 ==0 and num1 % 11 == 0:
    print("divisible")
else:
    print("not Divisible")