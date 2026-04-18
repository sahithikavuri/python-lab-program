try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Invalid input")
