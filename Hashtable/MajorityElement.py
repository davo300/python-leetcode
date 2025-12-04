class Solution(object):
    def majorityElement(self, nums):
       majEl = 0
       count = 0
       
       for i in range(len(nums)):
            if count == 0:
                majEl = i

            elif i == majEl:
                count += 1
                
            else:  
                count -= 1

       return majEl

       