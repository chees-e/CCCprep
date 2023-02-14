###########################################################################################
#
# > Question 1 Exercise 2
#
# > Description:
#         You are collecting apples, Your goal is to collect G apples. There are T apple 
#     trees, each can give K apples. You have a basket that can hold up to B apples. You 
#     want to know if you can collect enough apples from the trees with one trip.
#
# > Input Specification:
#         Input will four lines of input, in the following order: G, T, K, B.
#         0 <= T, K <= 1,000
#         1 <= G, B <= 1,000,000
#
# > Output Specification:
#         Output will be one line, True / False depending on whether or not you can collect
#     enough apples from the trees with your basket.
#
# > Sample Input 1:
#     20
#     3
#     5
#     30
#
# > Sample Ouput 1:
#     False
#
# > Sample Input 2:
#     20
#     5
#     7
#     15
#
# > Sample Output 2:
#     False
#
# > Run command:
#     python3 Q1/3_Solutions/A2.py
#
###########################################################################################

# Write your code here
G = int(input())
T = int(input())
K = int(input())
B = int(input())

met_goal = T * K >= G
can_fit = T * K <= B 

print(met_goal and can_fit)
















