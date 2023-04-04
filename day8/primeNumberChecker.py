def check_prime(number):
    for i in range(2,number):
        if number%i == 0:
                return("Not a prime number")
    return(f"{number} is prime")

n = int(input("Input a number ot check if it is prime: \n"))
print(check_prime(n))