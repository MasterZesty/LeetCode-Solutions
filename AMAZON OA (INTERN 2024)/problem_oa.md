Code Question - https://leetcode.com/discuss/interview-question/3114099/AMAZON-OA-(INTERN-2024)

Amazon Engineering maintains a large number of logs of operations across all products.
A software engineer is debugging an issue in a product. An efficient way to analyze logs
is to write automated scripts to check for patterns. The engineer wants to find the maximum
number of times a target word can be obtained by rearranging a subset of characters in a log entry.
Given a log entry s and target word t, the target word can be obtained by selecting some subset of
characters from s that can be rearranged to form string t and removing them from s. Determine the
maximum number of times the target word can be removed from the given log entry.
Note: Both strings s and t consist only of lowercase English letters.

Example
S = "mononom"
t="mon"
