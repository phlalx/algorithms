# Dynamic programming

## Exercise 1

For each of the following problems, give the recursive equations that can be 
used to solve the problem using dynamic programming.

### Tiling Problem

Count the number of ways to tile a "2 x n" board using "2 x 1" tiles.

Examples:

Input n = 3
Output: 3
Explanation:
There are three different way to tile the board.
1) Place all tiles vertically, 
2) Place one tile vertically on the left two tiles horizontally,
3) Place two tiles horizontally on the left and one tile vertically.

### Interleaving string 

Given s1, s2, s3, return true if s3 is formed by the interleaving of s1 and s2,
false otherwise.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false


### Longest well-parenthesed subsequence

Given a sequence of parenthesis, return the length of the longest subsequence for which parenthesis are well-balanced. 

Examples:

"()())()" -> 6 ( "()()()" or "(())()"  )
")(()" -> 2 ( "()"  )
")(" -> 0 ( "" )

### Decode ways

A message containing letters from A to Z is encoded to numbers, where each
letter is mapped to a number equal to its position in the alphabet.

'A' -> 1
'B' -> 2
...
'Z' -> 26

For instance, 'ALGO' is mapped to '112715'.

Given an encoded message containing digits, determine the total number 
of ways to decode it.

For example, encoded message "12", could be decoded as "AB" (1 2) or "L" (12).
Hence, the number of ways of decoding "12" is 2.

## Exercise 2

For exactly one of the previous problem:
* Write the dependency graph of the calls,
* Give the pseudo-code of a dynamic programming *iterative* implementation,
* Give its space and time complexity.


