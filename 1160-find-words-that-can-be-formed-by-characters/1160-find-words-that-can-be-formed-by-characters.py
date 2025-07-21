class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = {}
        for char in chars:
            charsMap[char] = charsMap.get(char, 0) + 1
        # print(charsMap)
        counter = 0
        for word in words:
            wordMap = {}
            for char in word: 
                wordMap[char] = wordMap.get(char, 0) + 1
            valid = True
            for char in wordMap:
                if wordMap[char] > charsMap.get(char, 0):
                    valid = False
                    break
            if valid:
                counter += len(word)
        return counter

            