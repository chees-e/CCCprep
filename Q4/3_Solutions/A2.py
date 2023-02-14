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
#     python3 Q4/3_Solutions/A2.py
#
###########################################################################################

# Write your code here

# Since s2 does not contain repeated letters, comparing sets is a good way to check for
# anagrams

s1 = input()
s2 = input()

set2 = set(s2)

# Set intersection keeps the elements that exist in both sets.
# So if the intersection didn't take out any elements, then two sets are the same.
for i in range(len(s1) - len(s2) + 1):
  cur = set(s1[i:i+len(s2)])
  if len(set2 & cur) == len(set2): # & is set intersection
    print(True)
    break
else:
  print(False)
  
  















