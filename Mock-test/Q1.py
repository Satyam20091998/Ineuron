def sqrt(x):
    if x <= 1:
        return x

    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid

    return right

# Testing the code
x = 4
print(sqrt(x))  # Output: 2

x = 8
print(sqrt(x))  # Output: 2
