# Define a function named Recurgcd that calculates the greatest common divisor (GCD)
# of two numbers 'a' and 'b' using recursion and the Euclidean algorithm
def Recurgcd(a, b):
    # Determine the lower and higher values between 'a' and 'b'
    low = min(a, b)
    high = max(a, b)

    # Check if the lower value is 0 (base case for GCD calculation)
    if low == 0:
        # If the lower value is 0, return the higher value (GCD is the non-zero value)
        return high
    # Check if the lower value is 1 (base case for GCD calculation)
    elif low == 1:
        # If the lower value is 1, return 1 (GCD of any number with 1 is 1)
        return 1
    else:
        # If neither base case is met, recursively call the Recurgcd function
        # with the lower value and the remainder of the higher value divided by the lower value
        return Recurgcd(low, high % low)

# Print the result of calling the Recurgcd function with the input values 12 and 14
print(Recurgcd(12, 14))
