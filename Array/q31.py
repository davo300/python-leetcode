'''
Topics:
Array
Two Pointers
'''
# apparently this problem sucks

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = None
        # for loop that iterates from right to left
        # range(start:stop:step) => step = -1 means reverse order
        for i in range(len(nums) - 1, 0, -1): 
            if nums[i] > nums[i - 1]:
                pivot = i - 1

                break
        # if we iterate through the entire for loop and we don't
        # break out of it, we can use else statement:
        else:   
            nums.reverse()

            return
        
        swap = len(nums) - 1
        while nums[swap] <= nums[pivot]:
            swap -= 1
        
        # swap the elements
        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        
        return
    
    #: Time: O(n) + O(n) = 2n -> O(n)
    #: Space: O(1)
    
        

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.nextPermutation(nums))  # Output: [1,3,2]
