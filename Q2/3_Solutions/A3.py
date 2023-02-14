###########################################################################################
#
# > Question 2 & 3 Exercise 3
#
# > Description:
#         Given A square on a 2D plane, and a list of points, determine how many 
#     coordinates are contained inside the sqaure. A coordinate c is contained inside a 
#     sqaure if bottom_left_corner <= c <= top_right_corner.
#
# > Input Specification:
#         First, there will be 3 lines of input. The first line will contain the x and y
#     coordinates of the bottom left corner of the sqaure, separated by a space. Next line
#     will contain an integer S, which will be the sqaure's side length. Next line will
#     contain N, which will be the number of points. Each of the next N lines will contain
#     the x and y values for the point.
#     1 <= side <= 1,000
#     1 <= N <= 100
#     -1,000 <= x, y <= 1,000
#
# > Output Specification:
#         Output will be one line with an integer equal to the number of points that lie
#     inside the sqaure
#
# > Sample Input 1:
#     0 0
#     5
#     3
#     4 5
#     3 3
#     0 1
#
# > Sample Ouput 1:
#     2
#
# > Sample Input 2:
#     -2 -1
#     1
#     1
#     -2 -1
#
# > Sample Output 2:
#     1
#
# > Run command:
#     python3 Q2/3_Solutions/A3.py
#
###########################################################################################

# Write your code here
square_x, square_y = input().split()
square_x, square_y = int(square_x), int(square_y)
side = int(input())
N = int(input())

ans = 0

for i in range(N):
  cur_x, cur_y = input().split()

  if square_x <= int(cur_x) <= square_x + side - 1:
    if square_y <= int(cur_y) <= square_y + side - 1:
      ans += 1

print(ans)

















