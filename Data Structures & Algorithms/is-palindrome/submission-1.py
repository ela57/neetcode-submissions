class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        i = 0
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            j -= 1
            i += 1
        return True
