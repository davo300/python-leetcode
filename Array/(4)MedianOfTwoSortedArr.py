class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge function
        def merge(S1, S2, S):
            ''' Merge two sorted Python lists S1 and S2 into properly sized list S. '''
            i = j = 0
            while i + j < len(S):
                if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
                    S[i+j] = S1[i]      # copy ith element of S1 as next item of S
                    i += 1
                else:
                    S[i+j] = S2[j]      # copy jth element of S2 as next item of S
                    j += 1


        # Merge-sort function
        def merge_sort(S):
            n = len(S)
            if n < 2:
                return      # list is already sorted
            # divide
            mid = n // 2    # floor division
            S1 = S[0:mid]   # copy of first half
            S2 = S[mid:n]   # copy of second half
            # conquer (with recursion)
            merge_sort(S1)  # sort copy of first half
            merge_sort(S2)  # sort copy of second half
            # merge results
            merge(S1,S2,S)  # merge sorted halves back into S
        
        # Main Logic
        nums3 = nums1 + nums2
        merge_sort(nums3)
        n = len(nums3)      # compute the median
        if n % 2 == 1:      # odd number of elements: middle element    
            median = nums3[n // 2]
        else:
            median = (nums3[n // 2 - 1] + nums3[n // 2]) / 2.0      # even number of elements: average of the two middle elements 
        # Return median as a string with 5 decimal places
        return round(median, 5)



def main():
    s = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(s.findMedianSortedArrays(nums1, nums2))
    


if __name__ == "__main__":
    main()