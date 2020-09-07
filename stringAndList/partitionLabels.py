'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.


'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        bucket = {} # hashmap to store the item and its last position
        
        #output = []
        #if len(S) <= 1 or len(set(S)) == len(S) : # no duplication in string
        #    output.extend([1 for _ in range(len(S))])
        #    return output 

        for i, v in enumerate(S):
            bucket[v] = i

        return self.findPart(S, bucket, [], 0)


    def findPart(self, S, bucket, output,i):
        if i >= len(S) or len(set(S[i:])) == len(S[i:]):
            output.extend([1 for _ in range(len(S[i:]))])
            return output 

        max_i = bucket[S[i]]+1

        seen = list(set(S[i+1:max_i]))

        bucket.pop(S[i])
        while seen:
            v = seen.pop(0)
            if v in bucket and bucket[v] >= max_i:
                diff = [char for char in S[max_i:bucket[v]+1]]
                max_i = bucket[v]+1
                bucket.pop(v)
                
                for val in set(diff):
                    if val in bucket:
                        seen.append(val)
        
        output.append(len(S[i:max_i]))

        return self.findPart(S, bucket, output, max_i)         
            


    def Test(self, S, expected):
        output = self.partitionLabels(S)
        print('testing on string:', S)
        print(output)
        if output == expected: return 'Pass'
        return 'Fail'


sol = Solution()
s = 'abcde'
print(sol.Test(s, [1, 1, 1, 1, 1]))
s = 'abaccbdeffed'
print(sol.Test(s, [6,6]))
s = 'ababcbacadefegdehijhklij'
print(sol.Test(s, [9,7,8]))
s = 'ababefgh'
print(sol.Test(s, [4,1,1,1,1]))

        

