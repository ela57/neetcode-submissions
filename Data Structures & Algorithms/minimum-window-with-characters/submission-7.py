class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            
            return ""
        hmap = defaultdict(int)
        for c in t:
            hmap[c] += 1
        missing = len(t)
        l, r = 0, 0
        mini = len(s) + 1
        bl, br = 0, 0
        while r < len(s):
            while r < len(s) and missing > 0:
                if s[r] in hmap:
                    if hmap[s[r]] > 0:
                        missing -=1
                    hmap[s[r]] -= 1

                r += 1
            while missing == 0:
                if r - l < mini:
                    bl = l
                    br = r
                    mini = r - l
                if s[l] in hmap:
                    hmap[s[l]] += 1
                    if hmap[s[l]] > 0:
                        missing += 1
                l += 1

        return s[bl:br]
