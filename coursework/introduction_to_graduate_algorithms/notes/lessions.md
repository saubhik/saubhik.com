# Notes
[Eric Vigoda]

# Dynamic Programming
We do not want to recompute the solutions to the small sub-problems.

## Longest Increasing Subsequence
Input: `n` numbers `a_1, a_2, ..., a_n` 
Goal: Find length of LIS in above sequence.  

Start by thinking of what could be a sub-problem.  Also mathematically
formalize it.  Call `L[i]` the LIS for subsequence `a[0]...a[i]`.  Then, think
if you know the answer to smaller subproblems, how can you construct answer to
a bigger problem. How can you find `L[i]` given you know `L[i-k]` for all `k
> 0`. Easier problems are simple. They might require knowledge of only `L[i-1]`.

So, we come up with this:

```
L[i] = L[i - 1] if a[i] <= a[i - 1] else L[i - 1] + 1.
```

Solve `Longest Increasing Subsequence` and `Longest Increasing Substring`
problems.
