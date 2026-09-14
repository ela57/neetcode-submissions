class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod , zero_cnt = 1,0

        for i in nums:
            if i:
                prod *= i
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for i in range(len(nums)):
            if zero_cnt:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0;
            else:
                res[i] = prod//nums[i]
        return res