class Solution:

    def encode(self, strs: List[str]) -> str:
        rtn = ""
        for s in strs:
            rtn += str(len(s)) + "#" + s  
        return rtn

    def decode(self, s: str) -> List[str]:
        listr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            listr.append(s[i:j])
            i = j

        return listr

