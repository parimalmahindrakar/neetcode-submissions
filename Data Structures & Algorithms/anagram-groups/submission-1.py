from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        grouped_anagrams: dict = defaultdict(list)
        A_ORD = ord('a')

        for s in strs:
            alphabates = [0] * 27
            for char in s:
                alphabates[ord(char) - A_ORD] += 1
            
            grouped_anagrams[tuple(alphabates)].append(s)

        return list(grouped_anagrams.values())

        
        


        