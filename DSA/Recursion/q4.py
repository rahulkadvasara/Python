# Define a function named factorial that calculates the factorial of a given number 'n'
def factorial(n):
    # Check if 'n' is less than or equal to 1
    if n <= 1:
        # If 'n' is 1 or less, return 1 (base case for factorial)
        return 1
    else:
        # If 'n' is greater than 1, recursively call the factorial function
        # to calculate the factorial of (n - 1) and multiply the result by 'n'
        return n * factorial(n - 1)

# Print the result of calling the factorial function with the input value 5
print(factorial(5))
