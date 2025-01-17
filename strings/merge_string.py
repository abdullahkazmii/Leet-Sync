def mergeAlternately(word1: str, word2: str) -> str:
    word = []
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        word.append(word1[i])
        word.append(word2[i])
    word.extend(word1[min_length:])
    word.extend(word2[min_length:])
    return "".join(word)


word1 = "abcdez"
word2 = "defgh"
print(mergeAlternately(word1, word2))  # Output: "aebfcdf"
