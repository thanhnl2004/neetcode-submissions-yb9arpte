class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = [[0] * 26 for _ in range(len(strs))]
        table = {}

        for i in range(len(strs)):
            bucket = buckets[i]
            s = strs[i]
            for c in s:
                index = ord(c) - ord('a')
                bucket[index] += 1
        
        for i in range(len(buckets)):
            bucket = tuple(buckets[i])
            if bucket not in table:
                table[bucket] = [strs[i]]
            else:
                table[bucket].append(strs[i])
        
        return list(table.values())

        