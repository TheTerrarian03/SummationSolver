# good resource to check against:
# https://www.mathsisfun.com/numbers/sigma-calculator.html

from sympy import symbols, sympify
import math

class Equation:
    def __init__(self, string_repr=""):
        self.string_repr = string_repr
    
    def set_equation(self, string_repr):
        self.string_repr = string_repr

    def solve_equation(self, num):
        equation = self.string_repr
        equation = equation.replace('^', '**')  # Replace '^' with '**' for exponentiation
        equation = equation.replace('√', 'math.sqrt')  # Replace '√' with 'sqrt'

        equation = equation.replace("x", str(num))  # Replace 'x' for the needed number

        return eval(equation)
    
    def __str__(self):
        return self.string_repr

class Summation:
    def __init__(self, constant: float, eq: str, start_val, end_val):
        self.constant = constant
        self.eq = Equation(eq)
        self.start_val = start_val
        self.end_val = end_val
    
    def solve(self):
        total = 0
        for i in range(self.start_val, self.end_val+1):
            eq_res = self.eq.solve_equation(i)
            if eq_res == None:
                exit()
            else:
                total += eq_res
            pass
        return total * self.constant

    def toString(self):
        return "{}∑{},({},{})".format(self.constant, self.eq, self.start_val, self.end_val)

    def __repr__(self):
        return f"Summation of: {self.toString()}"

    def __str__(self):
        return "Const: {}, Eq: {}, Start: {}, End: {}".format(self.constant, self.eq, self.start_val, self.end_val)

def exit(success=False):
    print("Program exited with a " + ("success" if success else "failure"))
    quit()

def insert_mult(expression):
    result = ''
    for i, char in enumerate(expression):
        if i > 0 and char.lower() == 'x' and expression[i - 1].isdigit():
            result += '*'
            result += char
        elif i < len(expression) - 1 and char.lower() == 'x' and expression[i + 1].isdigit():
            result += char
        elif i > 0 and char.isdigit() and expression[i - 1].lower() == 'x':
            result += char
        else:
            result += char
    return result

def parse_input_to_summation(input: str):
    ### parsing string for individual pieces
    # split left and right
    try:
        c, right = input.split("∑")
    except ValueError:
        print("You need to have one `∑` sign!")
        exit()

    # split right into equation and range
    try:
        eq, range = right.split(",")
    except ValueError:
        print("You need to have exactly 1 `,` separating your equation and range!")
        exit()
    
    if not range.startswith("("):
        print("Your range needs to start with a `(`!")
        exit()
    if not range.endswith(")"):
        print("Your range needs to end with a `)`!")
        exit()

    try:
        start, end = range[1:-1].split("->")
    except ValueError:
        print("Your range needs to have the start and end nums separated by a `->`!")
        exit()
    
    ### checking validity of information pieces
    # constant
    if c == "":
        c = 1
    
    try:
        c = float(c)
    except ValueError:
        print(f"The front constant must be a float, not {type(c)}!")
        exit()
    
    # equation
    try:
        eq = insert_mult(eq)
        sympify(eq, {'x': symbols('x')})
    except:
        print(f"Your equation, `{eq}`, isn't a valid equation! Please check the formatting and syntax used.")
        exit()
    
    # start value
    try:
        start = int(start)
    except ValueError:
        print(f"The starting value must be an integer, not {type(start)}!")
        exit()

    try:
        end = int(end)
    except ValueError:
        print(f"The ending value must be an integer, not {type(end)}!")
        exit()

    return Summation(c, eq, start, end)

# step 1: get the user's input for sum equation
user_eq = input("Please enter your summation equation you want to solve here:\n(Make sure to use only `x` for your variable)\nThe format is `[c]∑[equation],([start num]->[end_num])`\n> ")

# step 2: parse the equation. This is a big step
sum = parse_input_to_summation(user_eq)

# step 3: solve the summation for the range given
total = sum.solve()

print(total)

# 1∑-8x+3x^2,(0->6)