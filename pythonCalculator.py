import sys
# Kneepads2 - Dylan - 9/15/2020

print("\nCalculator\n=========================\nType 'exit' to quit\n")

while True:
    try:
        equation = input("Input equation: ")
        if (equation.lower() == 'exit'):
            print("Exiting..\n")
            sys.exit(0)
        result = eval(equation)
        print(f"Result: {result}\n")
    except (SyntaxError, NameError, ZeroDivisionError):
        print("Not a valid equation\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")
