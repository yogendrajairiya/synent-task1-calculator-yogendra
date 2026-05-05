while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2 if num2 != 0 else "Cannot divide by zero")
        else:
            print("Invalid operation")

    except:
        print("Invalid input")

    again = input("Continue? (y/n): ")
    if again != "y":
        break
    
    