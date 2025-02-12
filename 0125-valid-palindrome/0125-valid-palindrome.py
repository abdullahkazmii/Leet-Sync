class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ""

        for char in s:
            if char.isalnum():
                s2 += char

        left = 0
        right = len(s2) - 1

        while left < right:
            if s2[left] != s2[right]:
                return False
            left += 1
            right -= 1
        return True
        