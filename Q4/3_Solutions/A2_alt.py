###########################################################################################
#
# > Question 4 Exercise 2
#
# > Description:
#         Given two strings s1 and s2, determine whether or not s1 contains an anagram of 
#     s2. An anagram of a word is a word that can be spelt with the same letters but in a
#     different arrangement. You may assume there are no repeated letters in s2.
#
# > Input Specification:
#         There will be two lines of input. First line will contain the string s1, second 
#     line will contain the string s2.
#     1 <= len(s2) <= len(s1) <= 1,000
#
# > Output Specification:
#         Output will be True / False indicating whether or not s1 contains an anagram of 
#     s2.
#
# > Sample Input 1:
#     abdcab
#     cdb
#
# > Sample Ouput 1:
#     True
#
# > Sample Input 2:
#     abedat
#     abd
#
# > Sample Output 2:
#     False
#
# > Run command:
#     python3 Q4/3_Solutions/A2_alt.py
#
###########################################################################################

# Write your code here

# This solution can allow s2 to contain repeated letters.
# This is a more 'proper' way to solve this problem without using sets.
# It utilizes a sliding window and two letter frequency dicts.
import string

# Helper function to check if two frequency dicts are equal
# equal = anagram
def checkequal(dict1, dict2):
  for letter in dict1:
    if dict1[letter] != dict2[letter]:
      return False 
  return True

s1 = input()
s2 = input()

# Note, these lists' size caps at 26
freq1 = {}
freq2 = {}

for letter in string.ascii_lowercase: # or you can just type everything out
  freq1[letter] = 0
  freq2[letter] = 0

for i in range(len(s2)):
  freq1[s1[i]] += 1
  freq2[s2[i]] += 1

for i in range(len(s1)-len(s2)):
  if checkequal(freq1, freq2):
    print(True)
    break
  # update freq1 (slides the window):
  freq1[s1[i]] -= 1
  freq1[s1[i+len(s2)]] += 1
else:
  # Needs one last check
  print(checkequal(freq1, freq2))


















