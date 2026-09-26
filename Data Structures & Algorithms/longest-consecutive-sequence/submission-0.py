class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        numsset = set(nums)
        for num in numsset:
            if not num - 1 in numsset:
                count = 0
                while num + count in numsset:
                    count += 1
                if max < count:
                    max = count
        return max

                

