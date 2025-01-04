# Merge Strings Alternately

#   You are given two strings word1 and word2. 
#   Merge the strings by adding letters in alternating order, starting with word1. 
#   If a string is longer than the other, append the additional letters onto the end of the merged string.
#   Return the merged string.




class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergeWord = []
        
        combined = zip(word1, word2)
        
        for i in combined:
            mergeWord.append(i[0] + i[1])
            
        mergeWord.extend(word1[len(word2):])
        
        
        mergeWord.extend(word2[len(word1):])
        
        
        result = "".join(mergeWord)
        print(result)
        return result
        
        
        

Solution().mergeAlternately("ab", "pqrs")