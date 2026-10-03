class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_map = {}

        for string in strs:
            sorted_str = "".join(sorted(string)) 
            
            if sorted_str in hash_map:
                hash_map[sorted_str].append(string)
                continue
            
            
            hash_map[sorted_str] = [string] 
        
        return list(hash_map.values())

                

        
        