* For each i check if its prev char is almost equal aplohabet or not => where abs diff of current char and prev char is less than equal to 1.
* If almost equal found then we have to change the curr index char to a char diff from prev as well as diff from the next. So we increment the change count. We don't hv to care about the what the new char will be.
* Also if we change the char to a new one that means we are sure that the next char should not be checked so iterate one more to skip check for the immidiate next char.
​
#### Code
```python
int removeAlmostEqualCharacters(string word) {
int ans = 0;
for(int i = 1; i < word.size(); i ++){
if(abs(word[i] - word[i-1]) <= 1){ ans++; i++; }
}
return ans;
}
```
​
​
count = 0
for i in range(1,len(word)):
if ( abs( ord(word[i]) - ord(word[i-1]) ) <= 1):
count += 1
i +=1
return count
​