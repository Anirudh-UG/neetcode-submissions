class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash_map_s = {}
        hash_map_t = {}

        # first pass through s
        for char_s in s:
            if char_s in hash_map_s:
                hash_map_s[char_s] += 1
                continue
            hash_map_s[char_s] = 1
        
        # first pass through t 
        for char_t in t:
            if char_t in hash_map_t:
                hash_map_t[char_t] += 1
                continue
            hash_map_t[char_t] = 1

        return hash_map_s == hash_map_t            



        