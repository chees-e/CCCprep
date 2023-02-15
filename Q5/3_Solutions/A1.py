###########################################################################################
#
# > Question 5 Exercise 1
#
# > Description:
#         You are being placed in a M by N maze with obstacles. You start at the top left
#     corner (1, 1) and you want to get to bottom right corner (M, N). You employ the
#     following strategy: for every move you first choose direction (up, down, left
#     right), then keep going straight in that direction until you hit a obstacle or a
#     wall, then repeat the process by choosing a new direction. Determine whether or not
#     you are able to get to the goal by following this strategy.
#
#     Bonus 1: Determine the minimum number of moves required to reach the goal.
#     Bonus 2: Determine the type of moves required to reach the goal.
#
# > Input Specification:
#         The first two lines will contain integers M and N. Then, there will be M lines of
#     string of length N representing the maze. Obstacles will be represented by the
#     character "X" while empty spaces will be represented by the character ".". You may
#     assume (1, 1) and (M, N) are never "X".
#     2 <= M, N <= 500
#     0 <= obstacles <= M * N - 2
#
# > Output Specification:
#         Output will be one line of True / False which indicates whether or not you can
#     reach the goal.
#
# > Sample Input 1:
#     3
#     4
#     ..X.
#     ...X
#     X...
#
# > Sample Ouput 1:
#     True
#
# > Sample Input 2:
#     4
#     4
#     ..X.
#     ....
#     ....
#     ..X.
#
# > Sample Output 2:
#     False
#
# > Run command:
#     python3 Q5/3_Solutions/A1.py
#
###########################################################################################

# Write your code here

#TODO
M = int(input())
N = int(input())

maze = []

for i in range(M):
  maze.append(list(input()))

# need to check if we have been to a sqaure already
been = [(1, 1)]  # Method 1: Keep track of a list

# Method 2: change maze elements to indicate if we have been

dfs = []

dfs.append((0, 0))

while len(dfs) > 0:
  r, c = cur = dfs.pop()

  if r == M - 1 and c == N - 1:
    print(True)
    break

  # Check if we have been here already
  # Method 1
  if cur in been:
    continue
  else:
    been.append(cur)

  # Method 2
  if maze[r][c] == 'b':
    continue
  else:
    maze[r][c] = 'b'

  nr, nc = r, c
  while nc < len(maze[0]) - 1:
    if maze[nr][nc + 1] == "X":
      break
    nc += 1
  dfs.append((nr, nc))

  nr, nc = r, c
  while nc > 0:
    if maze[nr][nc - 1] == "X":
      break
    nc -= 1
  dfs.append((nr, nc))

  nr, nc = r, c
  while nr < len(maze) - 1:
    if maze[nr + 1][nc] == "X":
      break
    nr += 1
  dfs.append((nr, nc))

  nr, nc = r, c
  while nr > 0:
    if maze[nr - 1][nc] == "X":
      break
    nr -= 1
  dfs.append((nr, nc))
else:
  print(False)
