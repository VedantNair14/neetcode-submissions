class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Step 1: Sort the array
        # This is crucial for handling duplicates and using pointers
        nums.sort()

        for i, a in enumerate(nums):
            # Step 2: Skip the same value to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Step 3: Use two pointers for the rest of the array
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # We found a valid triplet!
                    res.append([a, nums[l], nums[r]])
                    
                    # Step 4: Update pointers and skip duplicates for 'l'
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res