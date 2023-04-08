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
def calculator():
    calculate = True
    n1 = float(input('Input first number:'))
    while calculate:
        for op in operations:
            print(op)
        operation = input('Input an Operation:')
        if operation not in operations:
            print("Invalid operation entered")
            calculator()
            
        n2 = float(input('Input another number:'))

        function = operations[operation]
        ans = function(n1, n2)
        print(f"{n1} {operation} {n2} = {ans}")

        cont = input(f'Do you want continue calculating with {ans}?(y/n)To quit press "q". \n')

        if cont == "n":
            calculator()
        elif cont == "y":
            n1 = ans
        else:
            calculate = False

calculator()