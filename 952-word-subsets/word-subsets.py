class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        n1 = len(words1)
        n2 = len(words2)
        ans = []


        maxcharfreq = [0]*26
        tempcharfreq = [0]*26

        for word in words2:

            for ch in word:
                tempcharfreq[ord(ch)-ord('a')] += 1

            for i in range(26):
                maxcharfreq[i] = max(maxcharfreq[i], tempcharfreq[i])

            tempcharfreq = [0]*26

        for word in words1:

            for ch in word:
                tempcharfreq[ord(ch)-ord('a')] += 1

            isuniversal = True

            for i in range(26):
                if maxcharfreq[i] > tempcharfreq[i]:
                    isuniversal = False
                    break

            if isuniversal:
                ans.append(word)

            tempcharfreq = [0]*26

        return ans
        