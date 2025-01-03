import time

def add(x,y):
    summ = x + y
    print(f"{x} + {y}  = {summ}")
    return summ

def sub(x,y):
    difference = x - y
    print(f"{x} - {y}  = {difference}")
    return difference

def mul(x,y):
    product = x * y
    print(f"{x} * {y}  = {product}")
    return product

def div(x,y):
    division = x / y
    print(f"{x} / {y}  = {division}")
    return division

starting_number = int(input("Give the first number: "))
print("+\n-\n*\n/")
operator_choser = input("Choose an operator: ")
if(operator_choser == '+'):
    second_number = int(input("Give the second number: "))
    result = add(starting_number,second_number)

elif(operator_choser == '-'):
    second_number = int(input("Give the second number: "))
    result = sub(starting_number,second_number)

elif(operator_choser == '*'):
    second_number = int(input("Give the second number: "))
    result = mul(starting_number,second_number)

elif(operator_choser == '/'):
    second_number = int(input("Give the second number: "))
    result = div(starting_number,second_number)

while True:
    decision = input("If want to continue doing operations with the result then type 'yes' or to start a new type 'no' and to exit type 'exit: ")

    if(decision == 'yes'):

        starting_number = result
        print("+\n-\n*\n/")
        operator_choser = input("Choose an operator: ")
        if(operator_choser == '+'):
            second_number = int(input("Give the second number: "))
            result = add(starting_number,second_number)

        elif(operator_choser == '-'):
            second_number = int(input("Give the second number: "))
            result = sub(starting_number,second_number)

        elif(operator_choser == '*'):
            second_number = int(input("Give the second number: "))
            result = mul(starting_number,second_number)

        elif(operator_choser == '/'):
            second_number = int(input("Give the second number: "))
            result = div(starting_number,second_number)

    elif(decision == 'no'):

        starting_number = int(input("Give the first number: "))
        print("+\n-\n*\n/")
        operator_choser = input("Choose an operator: ")
        if(operator_choser == '+'):
            second_number = int(input("Give the second number: "))
            result = add(starting_number,second_number)

        elif(operator_choser == '-'):
            second_number = int(input("Give the second number: "))
            result = sub(starting_number,second_number)

        elif(operator_choser == '*'):
            second_number = int(input("Give the second number: "))
            result = mul(starting_number,second_number)

        elif(operator_choser == '/'):
            second_number = int(input("Give the second number: "))
            result = div(starting_number,second_number)
    
    elif(decision == 'exit'):
        print("Closing Calculator")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        break