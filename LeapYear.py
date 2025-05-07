year = int(input("Enter a year: "))

def is_leap(year):

    leap : bool
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print(f"{year} is a leap year")
        leap = True
    else:
        print(f"{year} is not a leap year")
        leap = False
    return leap

print(is_leap(year))