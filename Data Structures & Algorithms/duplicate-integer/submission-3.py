class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = defaultdict(int)
        for n in nums:
            if hmap[n] > 0: return True
            hmap[n] += 1
     
        return False