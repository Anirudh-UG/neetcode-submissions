from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for s in strs:
            c = [0] * 26
            for char in s:
                c[ord(char) - ord("a")] += 1
            sol[tuple(c)].append(s)
        return list(sol.values())
                

        
        