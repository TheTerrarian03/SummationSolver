import math

def solve_equation(x_value, equation):
    equation = equation.replace('^', '**')  # Replace '^' with '**' for exponentiation
    equation = equation.replace('√', 'math.sqrt')  # Replace '√' with 'sqrt'

    equation = equation.replace("x", str(x_value))  # Replace 'x' for the needed number

    return eval(equation)

# Examples
print(solve_equation(5, "x.3^3-5"))