class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s2 = ""

        for i in s:
            if i.isalnum():
                s2+=i
        
        left, right = 0, len(s2)-1
        while left < right:
            if s2[left] != s2[right]:
                return False
            left+=1
            right-=1
        return True