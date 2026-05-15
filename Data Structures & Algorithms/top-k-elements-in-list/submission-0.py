
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Step 2: Build buckets
        # freq[i] will contain a list of numbers that appear 'i' times
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
            
        # Step 3: Extract top k frequent elements
        res = []
        # Loop backwards through the frequency buckets
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 