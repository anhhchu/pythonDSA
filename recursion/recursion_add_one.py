def add_one(array):
    if array == [9]:
        return [1,0]
    if array[-1] <9:
        array[-1]+=1
    else:
        array = add_one(array[:-1]) + [0]
    return array

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if add_one(arr) == solution:
        print('Pass')
    else:
        print('Fail')

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)
