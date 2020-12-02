def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, start = 0.0, 0
    for end in range(len(arr)):
        windowSum += arr[end]
        
        if end >= K-1: 
            result.append(windowSum/K)
            windowSum -= arr[start]
            start += 1
        

    return result


result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))

 
