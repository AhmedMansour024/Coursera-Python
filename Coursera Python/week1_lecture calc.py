def square_return(num):
    return num**2

def square_print(num):
    print("the square of num is",num**2)
    


def convert(input_str):
    # Replace :) with 🙂 and :( with 🙁
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_str

def main():
    user_input = input()
    result = convert(user_input)
    print(result)

# Call main function
main()

x, y, z = input().split()
operator = y
x = float(x)
z = float(z)

if operator == '+':
    result = x + z
elif operator == '-':
    result = x - z
elif operator == '*':
    result = x * z
elif operator == '/':
    if z == 0:
        print("Division by zero is not allowed.")
    result = x / z
    print(result)
else:
    print("Invalid operator. Please use +, -, *, or /.")
    