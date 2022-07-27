#6. Write python program that swap two number with temp variable and without temp variable.

# Python program to swap two variables

x = 5
y = 10

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# Without Using Temporary Variable

x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)
