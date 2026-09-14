class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cont = set()
        for num in nums:
            if num in cont:
                return True
            cont.add(num)
        return False
        
