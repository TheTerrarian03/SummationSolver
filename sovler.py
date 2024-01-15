def insert_multiplication_no_regex(expression):
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

print(insert_multiplication_no_regex("-8*x+3x^2"))