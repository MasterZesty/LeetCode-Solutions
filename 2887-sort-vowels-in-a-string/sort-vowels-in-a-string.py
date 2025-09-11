class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_pos = []
        vowels = []
        vowels_freq = {
            'a' : 0,
            'e' : 0,
            'i' : 0,
            'o' : 0,
            'u' : 0,
            'A' : 0,
            'E' : 0,
            'I' : 0,
            'O' : 0,
            'U' : 0,
        }

        for idx, char in enumerate(s):

            if vowels_freq.get(char, -1) != -1:
                vowels_freq[char] = vowels_freq.get(char, 0) + 1
                vowels_pos.append(idx)
                vowels.append(char)

        n = len(s)
        vowels.sort()
        # print(vowels)
        # print(vowels_pos)
        t = list(s)

        for pos, vowel in zip(vowels_pos,vowels):
            t[pos] = vowel


        return "".join(t)