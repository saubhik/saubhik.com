---
layout: post
title: Implement rand10() using rand7()
---

This is challenge for day 29 of August Leetcoding Challenge. Two approaches are discussed, *Rejection Sampling* and *Utilizing out-of-range samples*.

## Rejection Sampling

If we could generate a number in the desired range, output it immediately. Otherwise, reject it and re-sample.

We need to ensure uniform distribution.

Sample 2 times. It gives us `i` and `j` indices for:

|   | 1 | 2  | 3  | 4 | 5  | 6  | 7 |
|---|---|----|----|---|----|----|---|
| 1 | 1 | 2  | 3  | 4 | 5  | 6  | 7 |
| 2 | 8 | 9  | 10 | 1 | 2  | 3  | 4 |
| 3 | 5 | 6  | 7  | 8 | 9  | 10 | 1 |
| 4 | 2 | 3  | 4  | 5 | 6  | 7  | 8 |
| 5 | 9 | 10 | 1  | 2 | 3  | 4  | 5 |
| 6 | 6 | 7  | 8  | 9 | 10 |    |   |
| 7 |   |    |    |   |    |    |   |

When we encounter `i`, `j` corresponding to blank box, re-sample.

```python
class Solution:
    def rand10(self):
        while True:
            i, j = rand7(), rand7()
            idx = (i - 1) * 7 + j
            if idx < 41:
                return 1 + (idx - 1) % 10
```

This is $O(1)$ average time. And $O(\infty)$ in worst case. Space is $O(1)$.

The following was my first attempt, but does not get accepted since it's not uniform. Check the code comments.

```python
from random import randint

def rand7():
    return randint(1, 7)

class Solution:
    # abs(randint(1, 7) -  randint(1, 7)) is in [0, 6]
    # Need [0, 3].
    # int(abs(randint(1, 7) - randint(1, 7)) / 2) is in [0, 3]
    # 0/2=0, 1/2=0, 2/2=1, 3/2=1, 4/2=2, 5/2=2, 6/2=3
    # 3 has less probability of happening, so it is not uniform.
    def rand10(self):
        return int(abs(rand7() - rand7()) / 2) + rand7()
```

## Utilizing out-of-range samples

When we get an integer in the range $[41, 49]$; we have actually sampled uniformly from the range $[1, 9]$. Now, we can re-sample to get an integer in the range $[1, 63]$. 

If we get an integer between 1 to 60, we're done. If not, we have actually sampled uniformly from the range $[1, 3]$. We re-sample again to get an integer in the range $[1, 21]$.

If we get an integer between 1 to 20, we're done. If not, we re-start the entire process.

```python
class SolutionTwo:
    def rand10(self):
        while True:
            i, j = rand7(), rand7()
            idx = (i - 1) * 7 + j
            if idx < 41:
                return 1 + (idx - 1) % 10

            i, j = idx - 40, rand7()
            # i is in 1 to 9
            idx = (i - 1) * 7 + j
            if idx < 61:
                return 1 + (idx - 1) % 10

            i, j = idx - 60, rand7()
            # i is in 1 to 3
            idx = (i - 1) * 7 + j
            if idx < 20:
                return 1 + (idx - 1) % 10
```