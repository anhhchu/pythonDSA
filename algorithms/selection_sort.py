def selection_sort(L):
    if len(L)==0:
        return []
    temp = L[0]
    sub = L[1:]
    #L = []
    step = 0
    while sub:
        for i,val in enumerate(sub): #O(len(s))
            if val < temp:
                #L.append(val)
                sub[i] = temp
                temp = val

        #L.append(temp)
        L[step] = temp
        temp = sub[0]
        sub = sub[1:]
        print('step',step,temp, sub)
        #print(step, L)
        step+=1
    L[-1]=temp
    #print(L)
    return L

print('result:', selection_sort([9,8,7,6,1,3,5,7,12,0,0,0]))

print('result:', selection_sort([]))

'''BETTER IMPLEMENTATION'''
def selSort(L):
    store = 0
    while store!= len(L):
        for i in range(store, len(L)):
            if L[i]<L[store]:
                L[store],L[i] = L[i], L[store]
        store+=1
    return L

print('result selSort:', selSort([9,8,7,6,1,3,5,7,12,0,0,0]))
