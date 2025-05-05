import argparse

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operation == "multiply":
        result = multiply(args.num1, args.num2)
    elif args.operation == "divide":
        result = divide(args.num1, args.num2)
    else:
        result = "Invalid operation"

    print(f"Result: {result}"