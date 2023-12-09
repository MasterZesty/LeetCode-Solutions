## Approch 1

```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
        n = len(word)
        
        if n == 1:
            return 0
        
        if n == 2:
            if abs(ord(word[0]) - ord(word[1])) == 1:
                return 1
            
            if word[0] == word[1]:
                return 1
            
            return 0
            
        
        
        def is_almost_equal(a: str, b: str) -> bool:
            ans = a == b or abs(ord(a) - ord(b)) == 1
            print(f"a: {a} b: {b} => {ans}")
            return ans
        
        
        i = 0
        count = 0
        
        while i < n - 2:
            
            step_1 = is_almost_equal(word[i], word[i + 1])
            step_2 =  is_almost_equal(word[i+2], word[i + 1])
            print(f"for i: {i} {word[i]} and {word[i+1]} is almost equal s1 {step_1} and s2 {step_2}")
            
            if step_1 or step_2:
                count += 1
                possible_char = word[i + 1]
                print(f"entring step 1 with val {step_1} and possible_char {possible_char}")
                
                while is_almost_equal(word[i], possible_char) or is_almost_equal(word[i + 2], possible_char):
                    print(f"word: {word} | possible_char: {possible_char}")
                    possible_char = chr(ord(possible_char) + 1)
                    if possible_char == "A":
                        possible_char = "a"
                
                # Update the word with the modified character
                word = word[:i + 1] + possible_char + word[i + 2:]
            
            i += 1
        
        print(f"word: {word}")
        
        return count   
				
				
```

### the above code contaim a bug but logic wise if we see we are modifying the sring by finding the actual charecter. if we think carefully you will notice there is no need to find that char or modify the string


#### Approach

* Iterate from i = 1 to the string end.
* For each i check if its prev char is almost equal aplohabet or not => where abs diff of current char and prev char is less than equal to 1.
* If almost equal found then we have to change the curr index char to a char diff from prev as well as diff from the next. So we increment the change count. We don't hv to care about the what the new char will be.
* Also if we change the char to a new one that means we are sure that the next char should not be checked so iterate one more to skip check for the immidiate next char.

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
