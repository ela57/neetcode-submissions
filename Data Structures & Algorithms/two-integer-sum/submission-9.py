class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i, n in enumerate(nums):
            hashm[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashm and hashm[diff] != i:
                return [i, hashm[diff]]
        return []