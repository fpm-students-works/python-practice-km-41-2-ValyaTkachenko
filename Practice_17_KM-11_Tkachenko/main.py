from exp_root.exponentiation import exp2, exp3
from factorial.factorial import fact
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    while True:
        print("\nMenu: ")
        print("   1. Calculate factorial")
        print("   2. Calculate square")
        print("   3. Calculate cube")
        print("   4. Calculate square root")
        print("   5. Calculate cube root")
        print("   6. Calculate logarithm (log base a)")
        print("   7. Calculate natural logarithm (ln)")
        print("   8. Calculate base-10 logarithm (lg)")
        print("   9. Exit")

        option = input("Choose an option (1-9): ")

        if option == "1":
                a = int(input("Enter a natural number: "))
                if a < 0:
                    raise ValueError("The number must be positive.")
                print(f"Factorial: {fact(a)}")
            
        elif option == "2":
            try:
                x = float(input("Enter a number: "))
                print(f"Square of {x} is {exp2(x)}")
            except ValueError:
                print("Error: incorrect input.")
        elif option == "3":
                x = float(input("Enter a number: "))
                print(f"Cube: {exp3(x)}")
            
        elif option == "4":
            try:
                x = float(input("Positive number: "))
                if x < 0:
                    raise ValueError("The number must be positive.")
                print(f"Square root of {x} is {root2(x)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif option == "5":
                x = float(input("Enter a number: "))
                print(f"Cube root : {root3(x)}")
        elif option == "6":
            try:
                a = float(input("Enter the base (a > 0, a != 1): "))
                b = float(input("Enter the number (b > 0): "))
                print(f"Logarithm of {b} with base {a} is {log(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif option == "7":
            try:
                b = float(input("Enter the number (b > 0): "))
                print(f"Natural logarithm of {b} is {ln(b)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif option == "8":
            try:
                b = float(input("Enter the number (b > 0): "))
                print(f"Base-10 logarithm of {b} is {lg(b)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif option == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()