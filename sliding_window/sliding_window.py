# O(n) solution for finding
# maximum sum of a subarray of size k


def maxSum(arr, k):
    
    # length of the array
    n = len(arr)

    # n must be greater than k
    if n <= k:
        print("Invalid")
        return -1

    # Compute sum of first window of size k
    window_sum = sum(arr[:k])   # arr[start:stop:step] => stop after 4th element

    # first sum available
    max_sum = window_sum

    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        # we are essentially subtracting the element to be kicked out of the window
        # and then we add the new element to the window sum and check if the new
        # window has a larger sum than the old window. 
        # i.e. (window_sum - old_1st_index) + new_1st_index 
        # python order of operations makes this → (17 - 1) + 2 = 18
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))