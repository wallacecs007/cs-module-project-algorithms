'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    arr2 = []

    # Loops through once.
    for i in range(0, len(arr)):
        if arr[i] == 0:
            arr2.append(arr[i])
        else:
            arr2.insert(0, arr[i])

    # for i in range(0, len(arr) - 1):
    #     for j in range(0, len(arr) - 1):
    #         if arr[j] == 0:
    #             temp = arr[j]
    #             arr[j] = arr[j + 1]
    #             arr[j + 1] = temp

    return arr2


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
