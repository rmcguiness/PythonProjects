year = int(input("What year do you want to check? \n"))

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 :
            print("${year} IS a leap year!")
        else:
            print("${year} is NOT a leap year!")
    else:
        print("${year} IS a leap year!")
else:
    print("${year} is NOT a leap year!")
