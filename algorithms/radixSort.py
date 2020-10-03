def getDigit(num, i):
    '''
    obtain the digit at index i of the number
    '''
    return (num//10**i)%10

def radixSort(nums):
    
    # check edge case
    if len(nums) == 0:
        return nums
    
    
    maxAbs = max([abs(num) for num in nums])
    nums = [maxAbs + val for val in nums]  # O(n) time to rescontruct num, this will take care of negative value
    maxVal = max(nums)
    
    i = 0
    while i < len(str(maxVal)): # O(d) where d is the max number of digits in nums after converting

        countList = [0]*10
        output = [None]*len(nums)
  
        for val in nums: # O(n)
            digit = getDigit(val,i)       
            countList[digit] += 1
     
        #calculate prefix sum
        # O(b) with b is the base of the values in nums (base is 10: 0->9 in this case)
        countList = [sum(countList[:j+1]) for j in range(len(countList))] 
        
        # construct output from countList of indexes
        for val in reversed(nums): # O(n)
            digit = getDigit(val,i)
            idx = countList[digit]-1
            countList[digit] -= 1
            output[idx] = val

        nums = output # O(n) to copy data from outputList to nums
        
        i+=1
    nums = [val - maxAbs for val in nums]
    return nums
    
print(radixSort([20, 45, 75, 90, 402, 24, 2, 77]))
print(radixSort([20, 1045, -875, 90, -402, 224, 332, 777]))
print(radixSort([20]))
print(radixSort([]))
             