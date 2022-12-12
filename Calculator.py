
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
continue_calculating = True

n1 = int(input("Enter a number: "))

while continue_calculating:
    for operators in operations:
        print(operators)

    operator = input("Choose an Operation: ")

    n2 = int(input("Enter a number: "))

    calculation_function = operations[operator]
    answer = calculation_function(n1, n2)
    print(f"{n1} {operator} {n2} = {answer}")

    user_choice = input("Wanna Continue the Calculation Type 'Yes' or Type 'No'?  ").title()
    if user_choice == "Yes":
        n1 = answer
    elif user_choice == "No":
        print("Good Bye!")
        continue_calculating = False
    else:
        print("Invalid Input!")
        continue_calculating = False


