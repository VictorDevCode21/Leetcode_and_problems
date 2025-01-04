class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowels_in_word = [st for st in s if st in vowels]
                
        result = list(s)
        reversed_index = 0
        
        for j in range(len(s)):
            if s[j] in vowels:
                result[j] = vowels_in_word.pop()
                reversed_index +=1
                
        s = "".join(result)
        return s
        
Solution().reverseVowels("IceCreAm")