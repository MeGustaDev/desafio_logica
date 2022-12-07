import math

def binet_fib(n):
    fib_number = (((1+ math.sqrt(5)) / 2)**n - ((1 - math.sqrt(5)) / 2)**n) / math.sqrt(5)
    return fib_number

def main():
    user_input = int(input())
    output = binet_fib(user_input)
    print(round(output, 1))

main()