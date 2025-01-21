def isAnagram(s: str, t: str) -> bool:
    countS, countT = {}, {}
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True


# print(isAnagram("anagram", "nagaram"))


# string approach
def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


print(isAnagram2("anagram", "nagaram"))

print(isAnagram2("rat", "tar"))
