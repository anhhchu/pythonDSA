'''
Optimization over recursion.
Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial. For example, if we write simple recursive solution for Fibonacci Numbers, we get exponential time complexity and if we optimize it by storing solutions of subproblems, time complexity reduces to linear.

if we write simple recursive solution for Fibonacci Numbers, we get exponential time complexity and if we optimize it by storing solutions of subproblems, time complexity reduces to linear.
'''

def recFib(n):
    if n<= 1:
        return n
    return recFib(n-1) + recFib(n-2) #O(2^n)

def fibDP(n):
    f = {}
    f[0] = 0
    f[1] = 1
    i = 2
    while i <= n: # O(N) time, O(N) space with dictionary f to keep the value
        if i not in f:
            f[i] = f[i-1] + f[i-2]
        i += 1
    print(f)
    return f[n] 

print(recFib(7))
print(fibDP(7))
