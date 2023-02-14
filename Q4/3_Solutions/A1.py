###########################################################################################
#
# > Question 4 Exercise 1
#
# > Description:
#         You want to attend the most popular party in the city. In order to achieve your 
#     goal, you asked your friends to monitor the activity at each party and send you 
#     reports. A report has the following format: X people entered party ID, or, X people 
#     left party ID. Given a list of reports, determine the party ID with the most number 
#     of people, as well as how many people are present at the end of the report. Assume #       all party start with 0 people.
#
#
# > Input Specification:
#         There will be an unknown lines of input before the last line which will be 
#     "stop". Each line prior will be a report.
#     2 <= X <= 1,000
#     1 <= ID <= 100
#
# > Output Specification:
#         Output will be one line with two integers separated by a space. The first will 
#     represent the party ID with the most number of people at the end, the second will 
#     represent the number of people in that party. If there is a tie, choose the party 
#     with the lowest ID.
#
# > Sample Input 1:
#     3 people entered party 1
#     2 people entered party 2
#     2 people left party 1
#     end
#
# > Sample Ouput 1:
#     2 2
#
# > Sample Input 2:
#     2 people entered party 2
#     2 people entered party 1
#
# > Sample Output 2:
#     1 2
#
# > Run command:
#     python3 Q4/3_Solutions/A1.py
#
###########################################################################################

# Write your code here

# Dict{ID:people} would be helpful
parties = {}

while True:
  line = input()

  if line == "end":
    break

  inplist = line.split()

  num, direction, ID = int(inplist[0]), inplist[2], int(inplist[4])

  if ID not in parties:
    parties[ID] = 0

  if direction == "entered":
    parties[ID] += num 
  elif direction == "left":
    parties[ID] -= num 

highest_people = -1
highest_ID = -1

for ID in parties:
  if parties[ID] > highest_people:
    highest_people = parties[ID]
    highest_ID = ID
  elif parties[ID] == highest_people:
    if ID < highest_ID:
      highest_ID = ID 

print(f"{highest_ID} {highest_people}")

















