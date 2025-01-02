class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        m = len(queries)

        vowels = {
            'a' : 1,
            'e' : 1,
            'i' : 1,
            'o' : 1,
            'u' : 1,
        }


        sum_words = [0 for _ in range(n)]
        
        sum_words[0] = 1 if vowels.get(words[0][0], 0) == 1 and vowels.get(words[0][-1], 0) == 1 else 0

        for i, word in enumerate(words):
            if i > 0:
                # print(i,word)
                sum_words[i] += sum_words[i-1]
                if vowels.get(word[0], 0) == 1 and vowels.get(word[-1], 0) == 1:
                    sum_words[i] += 1

        # print(f"{words}")
        # print(f"{sum_words}")


        ans = [0 for _ in range(m)]

        for i, query in enumerate(queries):
            l = query[0]
            r = query[1]
            adjustment = 1 if vowels.get(words[l][0], 0) == 1 and vowels.get(words[l][-1], 0) == 1 else 0

            count = sum_words[r] - sum_words[l] + adjustment

            ans[i] = count 

        return ans 
