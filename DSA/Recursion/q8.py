# Define a function named harmonic_sum that calculates the harmonic sum up to 'n' terms
def harmonic_sum(n):
    # Check if 'n' is less than 2 (base case for the harmonic sum)
    if n < 2:
        # If 'n' is less than 2, return 1 (base case value for the harmonic sum)
        return 1
    else:
        # If 'n' is greater than or equal to 2, calculate the reciprocal of 'n'
        # and add it to the result of recursively calling the harmonic_sum function with 'n - 1'
        return 1 / n + harmonic_sum(n - 1)

# Print the result of calling the harmonic_sum function with the input value 7
print(harmonic_sum(7))

# Print the result of calling the harmonic_sum function with the input value 4
print(harmonic_sum(4))
