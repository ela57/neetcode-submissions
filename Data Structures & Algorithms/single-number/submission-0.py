from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rtn = reduce(xor, nums)
        return rtn