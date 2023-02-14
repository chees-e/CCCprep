###########################################################################################
#
# > Question 2 & 3 Exercise 4
#
# > Description:
#         Given three vertices of a triangle, find the longest side's side length.
#
# > Input Specification:
#         There will be 3 lines of input. Each will contain two integers x, y, separated
#     by a single space.
#     -1,000 <= x, y <= 1,000
#
# > Output Specification:
#         Output will be one line with a float equal to the length of the longest side.
#     round your answer to 2 decimal places: (print("%0.2f" % x))
#
# > Sample Input 1:
#     0 0
#     3 0
#     3 4
#
# > Sample Ouput 1:
#     5.00
#
# > Sample Input 2:
#     0 0
#     1 0
#     2 1
#
# > Sample Output 2:
#     2.24
#
# > Run command:
#     python3 Q2/3_Solutions/A4.py
#
###########################################################################################

# Write your code here
import math

x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()
x1, x2, x3, y1, y2, y3 = int(x1), int(x2), int(x3), int(y1), int(y2), int(y3)

# I will be square rooting after finding the longest side
side1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
side2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
side3 = (x3 - x1) ** 2 + (y3 - y1) ** 2

longest = math.sqrt(max(side1, side2, side3))

print("%0.2f" % longest)


# Alternatively:
# if side1 >= side2 and side1 >= side3:
#   print("%0.2f" % math.sqrt(side1))
# elif side2 > side3:
#   print("%0.2f" % math.sqrt(side2))
# else:
#   print("%0.2f" % math.sqrt(side3))


















