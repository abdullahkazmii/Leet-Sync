class Solution:
    def sortString(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        result = ""
    
        while sum(char_count.values()) > 0: 
            # Ascending phase (steps 1-3)
            last_char = ''
            while True:
                found = False
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char > last_char and char_count.get(char, 0) > 0:
                        result += char
                        char_count[char] -= 1
                        last_char = char
                        found = True
                        break
                if not found: 
                    break

            # Decendening phase (steps 4-6)
            largest_char = '{'
            while True:
                found = False
                for char in 'zyxwvutsrqponmlkjihgfedcba':
                    if char < largest_char and char_count.get(char, 0) > 0:
                        result += char
                        char_count[char] -= 1
                        largest_char = char
                        found = True
                        break
                if not found: 
                    break
        return result
