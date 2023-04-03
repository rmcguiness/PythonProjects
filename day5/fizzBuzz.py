range_nums = input('Input two numbers for the range to calculate FizzBuzz: ').split()
if len(range_nums) == 2:
    for number in range(int(range_nums[0]), int(range_nums[1])+1):
        num = int(number)
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0 :
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)