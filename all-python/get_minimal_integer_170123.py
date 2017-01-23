"""
Write a function:

def solution(A)

that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer
(greater than 0) that does not occur in A.

For example, given:

A[0] = 1
A[1] = 3
A[2] = 6
A[3] = 4
A[4] = 1
A[5] = 2
the function should return 5.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range
[−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not
counting the storage required for input arguments).

It's from
https://codility.com/programmers/lessons/4-counting_elements/missing_integer/
"""

def solution(A):
    positive_a = sorted([x for x in A if x > 0])
    if not positive_a:
        return 1
    elif positive_a[0] != 1:
        return 1
    else:
        for i, n in enumerate(positive_a[:-1]):
            if positive_a[i+1]- n >= 2:
                return n + 1
    return positive_a[-1] + 1

print(solution([1,3,6,4,1,2]))
