

def check_leap_year(year):
    if (year%400 ==0) or (year%100 != 0) and year%4 == 0:
        print("{} is a Leap Year".format(year))
    else:
        print("It is not a Leap Year")

year = int(input("Please Enter the Year:"))
check_leap_year(year)
