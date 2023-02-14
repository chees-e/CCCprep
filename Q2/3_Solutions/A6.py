###########################################################################################
#
# > Question 2 & 3 Exercise 6
#
# > Description:
#         A frog is trying to climb up a well that is X meters deep, starting on day 1. On 
#     the i-th, the frog will climb up i meters. But when the day is over, the frog will 
#     drop to 75% of its current height (rounded down). Determine on which day will the 
#     frog finally climb out of the well.
#
# > Input Specification:
#         The input will be the integer X.
#     1 <= X <= 1,000
#
# > Output Specification:
#         The output will be an integer i representing the day on which the frog climbs 
#     out.
#
# > Sample Input 1:
#     10
#
# > Sample Ouput 1:
#     5
#
# > Sample Input 2:
#     1
#
# > Sample Output 2:
#     1
#
# > Run command:
#     python3 Q2/3_Solutions/A6.py
#
###########################################################################################

# Write your code here
import math

X = int(input())
day = 0
height = 0

while True:
  day += 1
  height += day
  
  if height >= X:
    print(day)
    break

  height = math.floor(height * 0.75)













