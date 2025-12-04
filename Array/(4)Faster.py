class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
  
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A,B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):     
            A,B = nums2, nums1      # Make sure A is the smaller array

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2        # A
            j = half - i - 2        # B
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd case
                if total % 2:
                    return min(Aright, Bright)
                
                # even case i.e. [1,2,3,4,5,6] => (3+4)/2 = 7/2 = 3.5
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2   # we want decimal number 
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


def main():
    s = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(s.findMedianSortedArrays(nums1, nums2))
    


if __name__ == "__main__":
    main()