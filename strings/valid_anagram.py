def isAnagram(s: str, t: str) -> bool:
    length = min(len(s), len(t))
    sorted(s)
    sorted(t)
    for i in range(length):
        if s[i] == t[i]:
            return True
        else:
            return False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # Output: True
