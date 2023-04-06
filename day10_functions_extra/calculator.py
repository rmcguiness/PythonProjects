def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
calculate = True
while calculate:
    n1 = float(input('Input first number:'))
    for op in operations:
        print(op)
    operation = input('Input an Operation:')

    n2 = float(input('Input Second number:'))

    function = operations[operation]
    ans = function(n1, n2)
    print(f"{n1} {operation} {n2} = {ans}")

    cont = input('Do you wish to continue?(y/n) \n')

    if cont == "n":
        calculate = False
