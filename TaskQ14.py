#To fin the number of the days in a particular month
month_num = int(input("Enter a month number:"))
if month_num in (1,3,5,7,8,10,12):
    print(f"number of days in {month_num} is 31")
elif month_num in (4,6,9,11):
    print(f"Number of days in {month_num} is 30" )
elif month_num == 2:                       #since this month days depends on the year and is not same in all the years 
 year  = int(input("Enter the year:"))
 if year % 4 == 0 and ( not  year%100 ==0) or (year % 400 ==0): # to check whethet the year is a leap year or not
   print("number of days in 2 is 29")
 else:
    print("Number of the days in 2 is 28")
else:
    print("Invalid number choose correct month number")
#Inpput week day numbers and print the week day
num_week = int(input("Enter a week day number"))
if num_week == 0:
    print("today is sunday")
elif num_week == 1:
    print("Today is Monday")
elif num_week == 2:
    print("Today is Tuesday")
elif num_week == 3:
    print("Today is Wednesday")
elif num_week == 4:
    print("Today is Thrusday")
elif num_week == 5:
    print("Today is Friday")
elif num_week == 6:
    print("Today is Saturday")
else:
    print("Invalid week number!!") 




