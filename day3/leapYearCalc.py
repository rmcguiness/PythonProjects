year = int(input("What year do you want to check? \n"))

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 :
            print(f"{year} IS a leap year!")
        else:
            print(f"{year} is NOT a leap year!")
    else:
        print(f"{year} IS a leap year!")
else:
    print(f"{year} is NOT a leap year!")
