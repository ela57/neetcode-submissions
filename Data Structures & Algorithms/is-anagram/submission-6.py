class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = defaultdict(int)
        for c in s:
            hmap[c] += 1
        for c in t:
            if hmap[c] == 0: return False
            hmap[c] -= 1
        return True
        