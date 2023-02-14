###########################################################################################
#
# > Question 4 Exercise 3
#
# > Description:
#         The string "abc....xyz" (length: 26) is being cut X times and rearranged into a
#     new string S. When rearranging, the letters in each piece of the string must remain
#     in their original order. Given the rearranged string, determine the minimum number
#     of cuts required.
#
# > Input Specification:
#         There will be one line of input which will be the rearranged string.
#     S = anagram of "abc...xyz"
#     0 <= num of cuts <= 25
#
# > Output Specification:
#         Output an integer representing the minimum number of cuts needed.
#
# > Sample Input 1:
#     opqrstuvwxyzfghijklmnabcde
#
# > Sample Ouput 1:
#     2
#
# > Sample Input 2:
#     abcdefghijklmnopqrstuvwxyz
#
# > Sample Output 2:
#     0
#
# > Run command:
#     python3 Q4/3_Solutions/A3.py
#
###########################################################################################

# Write your code here
import string

line = input()
abc = string.ascii_lowercase
cuts = 0
indices = []
# Easier to work with numbers
for i in range(len(line)):
  indices.append(abc.index(line[i])) # ord(line[i]) also works

# A cut occurs when the next index isn't one more than current
for i in range(len(line) - 1):
  if indices[i] + 1 != indices[i + 1]:
    cuts += 1

print(cuts)
