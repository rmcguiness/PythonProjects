import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# FIRST TRY
# password = ""

# for l in range(0, nr_letters):
#     rand_index = random.randint(0, len(letters)-1)
#     password += letters[rand_index]
# for s in range(0, nr_symbols):
#     rand_index = random.randint(0, len(symbols)-1)
#     password += symbols[rand_index]
# for n in range(0, nr_letters):
#     rand_index = random.randint(0, len(numbers)-1)
#     password += numbers[rand_index]

# password = list(password)

# for i in range(0,1000):
#     rand_1 = random.randint(0, len(password)-1)
#     rand_2 = random.randint(0, len(password)-1)

#     temp= password[rand_1]
#     password[rand_1] = password[rand_2]
#     password[rand_2] = temp

# password = ''.join(password)
# print(f"Your random generated password is: {password}")

# OPTIMIZED
password = []
for l in range(0, nr_letters):
    password.append(random.choice(letters))
for n in range(0, nr_numbers):
    password.append(random.choice(numbers))
for s in range(0, nr_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
password = ''.join(password)

print(f"Your randomized password: {password}")
