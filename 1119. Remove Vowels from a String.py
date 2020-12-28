class Solution:
    def removeVowels(self, S: str) -> str:
        res = ""
        vowel = {'a','e','i','o','u'}
        for s in S:
            if s not in vowel:
                res += s
                
        return res