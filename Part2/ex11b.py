def math_operation(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

print(math_operation(10, 5, "add"))      
print(math_operation(10, 5, "multiply"))  
print(math_operation(10, 0, "divide"))    
print(math_operation(10, 5, "mod"))       
