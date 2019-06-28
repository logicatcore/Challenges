# Program working

# Task
Find the 2000th number in the Hexagonal arrangement as seen in the sample picture(problemExplanation.png),
which can divide the rest other 6 neighbouring numbers perfectly(remainder 0).

# Interpreter and language used
MatLab

# Order of Operations

 -> Reproduce the hexagonal arrangement of numbers as per the problem-
    -statement

 -> Identify the 6 neighbhouring numbers of all the numbers based on the-
    -logic of nearest 6 numbers

 -> check if the center number is infact a factor of the product of the-
    -6 neighbhouring numbers
     1) Find the prime factors of the center number and the surronding
     numbers
     2) If all the prime factors of the center are present in the prime
     factors of all the 6 neighbhouring numbers. Then the center number is a
     factor of the 6 other numbers

 -> stop the program when the 2000th number is found
