class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        numsset = set(nums)
        for num in numsset:
            if not num - 1 in numsset:
                count = 0
                while num + count in numsset:
                    count += 1
                out = max(count, out)
        return out

                

