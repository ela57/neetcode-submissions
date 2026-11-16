class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = defaultdict(int)
        hset = set(s1)
        for s in s1:
            hmap[s] += 1
        l, r = 0, 0
        while r < len(s2):
            if s2[r] in hmap:
                hmap[s2[r]] -= 1
                
            if l > 0 and s2[l - 1] in hset:
                hmap[s2[l - 1]] += 1
            print(hmap.values())
            if not any(hmap.values()):
                return True
            r += 1
            if r - l >= len(s1):
                l += 1
        return False