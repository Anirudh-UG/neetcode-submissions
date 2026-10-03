from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hash_map = {}

        # get frequency
        for number in nums:
            if number in hash_map:
                hash_map[number] += 1
                continue
            hash_map[number] = 1


        # hashed map with the key as count and value as elements which occur key times
        swapped_hash_map = defaultdict(list)
        for key, value in hash_map.items():
            swapped_hash_map[value].append(key)
        
        sorted_keys = list(swapped_hash_map.keys())
        sorted_keys.sort(reverse=True)
        for key in sorted_keys:
            result.extend(swapped_hash_map[key])
        
        return result[:k]          


        

