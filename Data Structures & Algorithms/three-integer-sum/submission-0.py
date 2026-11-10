class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        i = 0
        hashm = {}
        while i < len(nums):
            hashm[nums[i]] = i
            i += 1
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                val = -(nums[i] + nums[j])
                if val in hashm and hashm[val] > j:
                    out = [nums[i], nums[j], val]
                    output.add(tuple(sorted(out)))
                j += 1
            
            i += 1
        return [list(i) for i in output]
            