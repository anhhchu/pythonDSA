'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
'''

class Solution(object):
    def canCompleteCircuitBF(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        # complexity: O(n*k) time - k is the list of possible starting options, k<=n; O(n) space
        """
        # starting station needs to have gas[i] >= cost[i]
        # brute force: 
            # find the list of starting options (check gas >= cost condition) O(n)
            # with each starting option, travel to the next station until 
                # gas runs out (return -1) or 
                # travel back to the starting point (return starting option) 
        
        
        startingPoints = [i for i,g in enumerate(gas) if gas[i]>=cost[i]] #O(n)
        
        if not startingPoints:
            return -1
        
        for i in startingPoints: # O(k)
   
            s = 0
            cost2 = cost[i:len(cost)] + cost[:i] # O(n) space
            for j, g in enumerate(gas[i:len(gas)] + gas[:i]): # O(n)
                # calculate cost at each stop 
                s = s+g-cost2[j]
         
                if s < 0:
                    break # go to next starting Points as this one doesn't work
            if s >= 0:
                return i # no need to go to next iteration, starting point found
            
        return -1
    
    
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        Complexity: O(n) only 1 iteration with 2 variables O(1) space
        """
        # initiate totalTank, currentTank
        # for each iteration of gas, cost:
            # update total, curr += gas[i] - cost[i]
            # if currT < 0 => i+1 is next starting point and reset currT = 0
            
        # return -1 if totalTank < 0 or startingStation otherwise
        
        totalT, currT = 0, 0
        startingP = 0
        for i in range(len(gas)): # O(N)
            totalT += gas[i] - cost[i]
            currT += gas[i] - cost[i]
            
            if currT < 0: # cannot reach next station, set next station = starting point
                startingP = i+1
                currT = 0
                
        # after the iteration, check totalT
        return startingP if totalT >= 0 else -1
        
        
sol = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(sol.canCompleteCircuit(gas, cost))
print(sol.canCompleteCircuitBF(gas, cost))