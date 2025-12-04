        def backTrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    # using recursion here to constantly pop and add back elements to the 
                    # freqMap and check if the len(perm) == len(nums) => means we have 
                    # found a unique permutation.
                    backTrack()     
    
                    count[n] += 1   # updating freqMap
                    perm.pop()      

        backTrack()
        return res