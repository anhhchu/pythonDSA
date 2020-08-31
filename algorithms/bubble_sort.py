def bubble_sort(L):
    swap = False
    step = 0
    while not swap: #O(len(L))
        swap = True
        for j in range(1,len(L)): #O(len(L))
            #print(swap, j)
            if L[j-1]>L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
            step += 1
            print(step, swap, j,L)
    return L

bubble_sort([10,9,8,7,6,5,4])
