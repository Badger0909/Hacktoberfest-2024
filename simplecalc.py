def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculate_bmi(weight, height):
    if height <= 0:
        return "Height must be greater than zero."
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def graph_linear_equation(slope, intercept):
    try:
        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(-10, 10, 100)  # Generate x values from -10 to 10
        y = slope * x + intercept  # Calculate corresponding y values

        plt.plot(x, y, label=f'y = {slope}x + {intercept}')
        plt.axhline(0, color='black', lw=1)  # Add x-axis
        plt.axvline(0, color='black', lw=1)  # Add y-axis
        plt.title('Graph of Linear Equation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.legend()
        plt.show()
    except ImportError:
        print("Error: matplotlib is not installed. Please install it using 'pip install matplotlib'.")
    except Exception as e:
        print(f"An error occurred while plotting the graph: {e}")

def main():
    print("Welcome to the Simple Calculator")
    
    while True:
        print("\nChoose an option:")
        print("1. Arithmetic Operations")
        print("2. Calculate BMI")
        print("3. Graph Linear Equation")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if operator == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operator == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operator == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operator == '/':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid operator.")
        
        elif choice == '2':
            weight = float(input("Enter your weight (in kg): "))
            height = float(input("Enter your height (in meters): "))
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi}")
        
        elif choice == '3':
            slope = float(input("Enter the slope of the line (m): "))
            intercept = float(input("Enter the y-intercept of the line (b): "))
            graph_linear_equation(slope, intercept)
        
        elif choice == '4':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
