class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in countS and countS[c1] != c2) or (c2 in countT and countT[c2] != c1)):
                return False
            countS[c1] = c2
            countT[c2] = c1
        return True
            