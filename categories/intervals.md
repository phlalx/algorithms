# Intervals

* merge a list of intervals !56
    - sort list by left value then greedy
    - or sort the edges (edge, 1,-1) with +1,-1 for start/end
* minimal overlapping of intervals to remove !435 (variant of !56)
* merge two list of intervals !986
    - variant on merge sort
* maximal number of overlapping interval
    - sort the edges (edge, 1/-1), with +1, -1 for start/end
* intervals coverage (minimal points such that all intervals contain one point)
    - sort intervals by right value then greedy
* interval tree (TODO but probably out of scope)
    - divide interval in tree categories based on some "center value"
    - L tree, R tree, root node (center, C)
    - Intervals in C are sorted in two lists (by start, by end). If the value
      we look for is greater than center, or lower, we use binary search in
      one of the two lists


## Sorting of intervals

By opening value

   ------
     --
            ----
                  ----
                    --------
                         --

By closing value

     --
   ------
            ----
                  ----
                         --
                    --------

To see the difference, use two dimensions.