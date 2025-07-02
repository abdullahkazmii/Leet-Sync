class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in anagram_groups:
                anagram_groups[key].append(word)
            else:
                anagram_groups[key] = [word]

        return list(anagram_groups.values())