class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Step 1: Determine which half is "normally" sorted
            if nums[l] <= nums[mid]:
                # Left side is sorted
                if target > nums[mid] or target < nums[l]:
                    # Target is in the right half
                    l = mid + 1
                else:
                    # Target is in the left half
                    r = mid - 1
            else:
                # Right side is sorted
                if target < nums[mid] or target > nums[r]:
                    # Target is in the left half
                    r = mid - 1
                else:
                    # Target is in the right half
                    l = mid + 1
        
        return -1