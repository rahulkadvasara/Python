# Define a function named fibonacci that calculates the nth Fibonacci number
def fibonacci(n):
    # Check if n is 1 or 2 (base cases for Fibonacci)
    if n == 1 or n == 2:
        # If n is 1 or 2, return 1 (Fibonacci sequence starts with 1, 1)
        return 1
    else:
        # If n is greater than 2, recursively call the fibonacci function
        # to calculate the sum of the (n-1)th and (n-2)th Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print the result of calling the fibonacci function with the input value 7
print(fibonacci(7))
