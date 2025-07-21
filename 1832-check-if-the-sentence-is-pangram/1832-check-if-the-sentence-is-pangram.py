class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique_letters = set(sentence)
        return len(unique_letters) == 26
        