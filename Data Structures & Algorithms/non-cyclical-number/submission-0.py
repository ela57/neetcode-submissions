class Solution:
    def isHappy(self, n: int) -> bool:
        hashs = set()
        while n != 1:
            if n in hashs:
                return False
            hashs.add(n)
            nstr = str(n)
            n = 0
            for i in range(len(nstr)):
                n += int(nstr[i]) * int(nstr[i])
        return True

