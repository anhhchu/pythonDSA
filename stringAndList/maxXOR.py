# -*- coding: utf-8 -*-
'''
Maximum XOR of Two Numbers in an Array
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

nums = [3, 10, 5, 25, 2, 8]

n = 3^10
print(n)
'''
trie = {}
for num in nums:
    node = trie
    for bit in num:
        if not bit in node:
            node[bit] = {}
        node = node[bit]
'''