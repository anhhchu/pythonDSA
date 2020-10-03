class Solution(object):
    def carPoolingBruteForce(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        O(max point - min point) time and space -- very bad
        """
        # create a hash with key from max start to max end of the trips 
        # for each key, count the number of passengers
        # if num passengers > capacity at any point, return False
        # else return True 
        # if the trips are not connected, also return False
        
        if len(trips) < 1: 
            return False
        if len(trips) == 1:
            if trips[0][0] <= capacity:
                return True
            else:
                return False
            
        points = {}
        for n, start, end in trips:
            
            if n > capacity:
                return False
            
            for p in range(start, end):
       
                if p in points:
                    points[p] = points[p] + n
                    if points[p] > capacity: 
                        return False 
                else:
                    points[p] = n

        return True

    def carPoolingOpt(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # bucket sort

        maxMile = 0
        for _,_,end in trips: # O(N) time
            maxMile = max(maxMile, end)
        
        print(maxMile)
        
        miles = [0] * (maxMile+1) # O(maxMile) space
        
        for n, start, end in trips: #O(N) time
            miles[start] += n
            miles[end] -= n 
           
        print(miles)
        usedCapacity = 0
        
        for n in miles: # O(maxMile) time
            usedCapacity += n
            if usedCapacity > capacity:
                return False
            
        return True
            

sol = Solution()
print(sol.carPoolingOpt([[3,2,7],[3,7,9],[8,3,9]],11))
    
        