###########################################################################################
#
# > Question 2 & 3 Exercise 5
#
# > Description:
#         Given two rectangles on a 2D plane, determine the area of their overlap. If they
#     do not overlap, the area is 0.
#
# > Input Specification:
#         There will be 4 lines of input, each with 2 integers separated by a single space,
#     representing the X and Y coordinate of a point. The first and second line contain the
#     coordinates for the bottom-right and top-left corner of rectangle 1, and the next two
#     lines contain the coordinates for the same corners of rectangle 2.
#     -1,000 < X, Y <= 1,000
# > Output Specification:
#         Output will be one integer representing the area of the overlap
#
# > Sample Input 1:
#     1 1
#     2 2
#     -2 -2
#     1 2
#
# > Sample Ouput 1:
#     2
#
# > Sample Input 2:
#     0 0
#     1 1
#     2 0
#     2 4
#
# > Sample Output 2:
#     0

# > Sample Input 3:
#     0 0
#     5 5
#     2 2
#     3 3
#
# > Sample Output 3:
#     4
#
# > Run command:
#     python3 Q2/3_Solutions/A5.py
#
###########################################################################################

# Write your code here

minx1, miny1 = input().split()
maxx1, maxy1 = input().split()
minx2, miny2 = input().split()
maxx2, maxy2 = input().split()

minx1, miny1 = int(minx1), int(miny1)
maxx1, maxy1 = int(maxx1), int(maxy1)
minx2, miny2 = int(minx2), int(miny2)
maxx2, maxy2 = int(maxx2), int(maxy2)

# Not overlapping
if minx1 > maxx2 or minx2 > maxx1 or miny1 > maxy2 or miny2 > maxy1:
  print(0)
else:
  # Find the largest min x/y and smallest max x/y
  # those will be the bound for the overlap
  minx = max(minx1, minx2)
  maxx = min(maxx1, maxx2)
  miny = max(miny1, miny2)
  maxy = min(maxy1, maxy2)

  area = (maxx - minx + 1) * (maxy - miny + 1)

  print(area)

# Explanation:
# If the two rectangles overlap, the overlap will be bounded by:
# On the left side, the biggest (or right most) minx (left bound) of the two rects
# On the right side, the smallest (left most) maxx (right bound) of the two rects
# Similar for up and down








