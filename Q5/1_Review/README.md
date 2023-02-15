# Question 5

### Essential Skills:

- ** 2D list operations
- ** Search
  - (iterative / recursive)
  - (DFS / BFS)
- Dynamic programming
- Divide and Conquer
- Sorting
- List comprehension (not necessary)
  - `lst = [i for i in range(lst) if i % 2 == 0]`
    
### Tips:

- There are two types of questions that almost always show up for question 5:
  - 2D problem
  - Search problem
  - Both combined
- Think about what search technique should be used
  - BFS: queue (`todo.pop(0)`), search for the shortest paths first, used for when you want to find a minimum/shortest solution
  - DFS: stack (`todo.pop()`), search for the longest paths first, used when you need a solution with fixed steps
- I recommend using an iterative approach (with the 'todo' list, or frontier), but you can use recursion if you are more comfortable with it
- Recursion is still important: for example divide and conquer algorithms (2022 CCC P5)
- 2D lists are quite common, make sure you know how to construct one, and iterative through one using double for loop
- Again, if you don't know how to start, try to focus on the part marks first. Often times they can be solved easier (like brute force)
- Look at the input constraints, try to work around the input that has a tighter constraint.