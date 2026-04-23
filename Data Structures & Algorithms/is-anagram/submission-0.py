class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A_ORD = ord('a')
        alphabate_indexes_s = [0] * 26
        alphabate_indexes_t = [0] * 26
        
        for char in s:
            alphabate_indexes_s[ord(char) - A_ORD] += 1
            
        for char in t:
            alphabate_indexes_t[ord(char) - A_ORD] += 1
        
        return alphabate_indexes_s == alphabate_indexes_t




        