##Code Question - https://leetcode.com/discuss/interview-question/3114099/AMAZON-OA-(INTERN-2024)
##
##Amazon Engineering maintains a large number of logs of operations across all products.
##A software engineer is debugging an issue in a product. An efficient way to analyze logs
##is to write automated scripts to check for patterns. The engineer wants to find the maximum
##number of times a target word can be obtained by rearranging a subset of characters in a log entry.
##Given a log entry s and target word t, the target word can be obtained by selecting some subset of
##characters from s that can be rearranged to form string t and removing them from s. Determine the
##maximum number of times the target word can be removed from the given log entry.
##
##Note: Both strings s and t consist only of lowercase English letters.
##
##Example
##S = "mononom"
##t="mon"
## 

# s = 'mononom'
# t = 'mon'

# Define the function to count the character occurrences in the string
def count_char_occurrences(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == "__main__":
    s = input()
    t = input()
    
    mp1 = count_char_occurrences(s)
    mp2 = count_char_occurrences(t)

    cnt = float('inf')

    for char in t:
        if char not in mp1:
            # it means char is not present in s hence we will not get any subset
            print(0)
            break

        val = mp1[char] // mp2[char]
        cnt = min(cnt, val)

    else:
        print(cnt)
    
