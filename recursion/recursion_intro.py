def recursive(input):
    if input < 0:
        return input
    else:
        output = recursive(input-1)
        print('output', output)
        return output

print(recursive(-2))

def power_of_2(n):
    if n==0:
        return 1
    else:
        return 2*power_of_2(n-1)

print(power_of_2(5))

def sum_integers(n):
    if n == 1:
        return 1
    else:
        return n+sum_integers(n-1)

print(sum_integers(990))
print(power_of_2(150))

def sum_array(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0]+sum_array(array[1:])

print(sum_array([1,2,3,4,5,6,7,8,9,10]))
print(sum_integers(10))

def sum_array_index(array,index):
    if len(array)-1 == index:
        return array[index]
    else:
        return array[index]+sum_array_index(array,index+1)

print(sum_array_index([1,2,3,4,5,6,7,8,9,10,20],0))

