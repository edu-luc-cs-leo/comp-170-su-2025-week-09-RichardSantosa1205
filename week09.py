def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW

def sum_of_digits(n):
    """
    Recursively returns the sum of the digits of n
    """
    # Handle negatives
    n = abs(n)

    # Store result in this variable
    result = 0

    if n < 10:
        # This is base case
        result = n
    else:
        # Grab the last digit, then perform recursion on the rest of the numbers.

        last_digit = n % 10
        remaining = n // 10
        result = last_digit + sum_of_digits(remaining)

    # Return the result of the recursion
    return result

print("sum_of_digits:")
print(sum_of_digits(789))
print(sum_of_digits(123))
print(sum_of_digits(0))
print(sum_of_digits(9876654))

def count_occurrences(data_list, target):
    """
    Recursively counts how many times target appears in data_list.
    """

    # Store result here
    result = 0

    if len(data_list) == 0:
        # This is base case
        result = 0
    else:
        # Grab the first item, and then pass in the rest of the items to the next iteration of the recursion.
        first_item = data_list[0]
        rest_of_list = data_list[1:]

        # If an occurence is found, add one.
        if first_item == target:

            result = 1 + count_occurrences(rest_of_list, target)
        else:
            result = count_occurrences(rest_of_list, target)

    return result

print("count_occurrences:")
print(count_occurrences([1,2,3,4,4,5,6,7,8,1,1,1,2,2,3], 1))
print(count_occurrences([1,2], 1))
print(count_occurrences([], 1))

def factorial_iterative(n):
    """
    Computes n! using an iterative loop.
    """
    
    # Store the result in this variable
    result = 1 

    # Since result is always 1, we can start multiplying from 2 until n.
    # Range is until n+1 because we want to include n
    for i in range(2, n + 1):
        result *= i

    return result

print("factorial_iterative:")
print(factorial_iterative(5))
print(factorial_iterative(2))
print(factorial_iterative(1))
print(factorial_iterative(10))


def fibonacci_iterative(n):
    """
    Computes F(n) iteratively where F(1)=1, F(2)=2, and F(n)=F(n-1)+F(n-2).
    """

    # Store the results in this variable
    result = 0

    if n <= 0:
        # Check if n is a valid number
        result = 0
    elif n == 1 or n == 2:
        # If n is either 1 or 2, just set the result to be 1 or 2
        result = n
    else:
        prev_two = 1 # this will be F(1)
        prev_one = 2 # this will be F(2)

        # Since we already know the values of F(1) and F(2), we can start from index 3
        i = 3

        # Now perform the Fibonacci sequence until F(n) is achieved.
        while i <= n:
            current = prev_one + prev_two
            prev_two = prev_one
            prev_one = current
            i = i + 1

        # Store the value which will be returned at the end.
        result = prev_one

    return result

print("fibonacci_iterative:")
print(fibonacci_iterative(5))
print(fibonacci_iterative(6))
print(fibonacci_iterative(7))
print(fibonacci_iterative(8))
