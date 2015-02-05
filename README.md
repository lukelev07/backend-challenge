# backend-challenge
Implementation of shifted list search.


### Problem Statement

The problem is to take a "shifted" python list, and to output the maximum element in said list. 

* Input: a sorted python list that has been shifted at some unspecified index, such that the end of the list wraps around to the beginning again.
* Output: the maximum element of the shifted list.

### Solution:

In essence, I have used a modified version of the classic binary search algorithm, which is essentially run on a sorted list of integers. The changes I have made to accommodate this problem are:

* Case to check if the list is indeed sorted and not shifted.
* Case to check if the midpoint is the max element desired.
* Boundary conditionals such that an out-of-bounds access is avoided.

#### Running time:

* Expected: O(log n) 
* Worst-case: O(n) (see shifted.py for explanation)

### Technical Reasoning: 

I chose Python 2 due to my experience in the past with it, and my familiarity with testing in the Python environment.

Initially I realized I could simply linearly scan to find the max, but then I noticed how this problem closely resembled binary search, so I modified the algorithm to handle this case. I wrote several test-cases, which I believe sufficiently show the completeness of this solution.
