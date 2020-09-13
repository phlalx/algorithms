# General form

In many problems, the input defines a large (potentially infinite) set of
states by comprehension. The algorithm has to somehow explore the set in
order to compute a function.

## Examples

### 8-queens

Input is `n`, the size of the board. It defines the set of possible
positions for `n` queens. Count the number of position satisfiyng the property.

### Le compte est bon

Input is a list of numbers and a target. The problem consists of finding if
an arrangement of the numbers and arithmetic operations can lead to a given
number. The set to explore is the  set of all arrangements.

### zero-sum

Input is an array. Find a sub-set whose sum is equal to zero.

### Solve the maze

Find a way in a maze. Input is a 2D grid. It defines the set of all paths.

# Brute force