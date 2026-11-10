class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        hmap = {}
        while i < len(nums):
            hmap[target - nums[i]] = i
            i += 1
        for i in range(len(nums)):
            n = nums[i]
            if n in hmap and i != hmap[n]:
                return [i, hmap[n]]



            