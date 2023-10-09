#This exercise will walk you through how to write a list comprehension to create a list of squared numbers (n*n). It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively. For example, squares(2, 3) should return a list containing [4, 9].

#The function receives the variables “start” and “end” through the function parameters.

#In the return line, start by entering the list brackets [ ]

#Between the brackets [ ], enter the arithmetic expression to square a variable “n”.

#To the right of the square expression, write a for loop that iterates over “n” in a range from the “start” to “end” variables.

#Ensure the “end” range value is included in the range() by adding 1 to it.

def squares(start, end):
    return [n*n for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

