print("My Calculator")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter a mathematical operaration (+, -, *, /): ")

operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2
}

print("The result is: ", operations[operation])


