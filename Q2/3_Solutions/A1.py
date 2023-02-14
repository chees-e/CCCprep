###########################################################################################
#
# > Question 2 & 3 Exercise 1
#
# > Description:
#         You are inventing a new way to encrypt a sequence of numbers. For every 1 or 2
#     digits in the sequence, you can turn them into two single digit integers 
#     whose product is the 1 or 2 digit number. For example 42 can turn into 
#     76 (7 x 6 = 42), 5 can be turn into 15 (1 x 5 = 5). Given an encrypted sequence, 
#     output the original sequence.
#
#
# > Input Specification:
#         Input will one line of sequence of integers.
#     2 <= length <= 2,000
#
# > Output Specification:
#         Output will be one line of decrypted sequence of integers.
#
# > Sample Input 1:
#     34671355
#
# > Sample Ouput 1:
#     1242325
#
# > Sample Input 2:
#     98064023
#
# > Sample Output 2:
#     72006
#
# > Run command:
#     python3 Q2/3_Solutions/A1.py
#
###########################################################################################

# Write your code here

# we should keep it as a string to accesses digit by digit
encrypted = input()
result = "" # string building

for i in range(0, len(encrypted), 2):
  n1 = int(encrypted[i])
  n2 = int(encrypted[i+1])

  product = str(n1 * n2)
  result += product

print(result)













