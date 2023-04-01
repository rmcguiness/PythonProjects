print('Welcome to Python Pizza Delivery')
size = input('What size pizza do you want? S, M, L')
add_pepperoni = input('Would you like to add pepperoni to you pizza? Y,N')
extra_cheese = input('Do you want extra cheese? Y,N')

bill = 0

if size == 'S' :
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total is {bill}")