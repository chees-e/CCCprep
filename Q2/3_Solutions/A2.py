###########################################################################################
#
# > Question 2 & 3 Exercise 2
#
# > Description:
#         One day, a group of N friends tried an experiment where they each paid for 
#     another person's groceries. Given N integers representing the cost of each person's 
#     groceries, determine the number of people who paid more for the other person's 
#     groceries than if they only paid for their own.
#
# > Input Specification:
#         The first line of input will contain an integer N. There will be N lines of input
#     following the first. Each line will contain an integer equal to a person's grocery
#     cost. The person at line i will pay for the person at i+1's groceries, with the last
#     person paying for the first person's groceries.
#     1 <= N <= 100
#     1 <= price <= 1,000
#
# > Output Specification:
#         Output will be one line with an integer equal to the number of people who spent
#     more money due to the experiment.
#
# > Sample Input 1:
#     5
#     2
#     3
#     4
#     5
#     3
#
# > Sample Ouput 1:
#     3
#
# > Sample Input 2:
#     3
#     2
#     2
#     2
#
# > Sample Output 2:
#     0
#
# > Run command:
#     python3 Q2/3_Solutions/A2.py
#
###########################################################################################

# Write your code here
N = int(input())

first = int(input())
costs = [first,]

ans = 0

for i in range(N-1):
  cur = int(input())
  if costs[-1] < cur:
    ans += 1
  costs.append(cur)

# Last person paying for first person
if costs[-1] < costs[0]:
  ans += 1

print(ans)
  














