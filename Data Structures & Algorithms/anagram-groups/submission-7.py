class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        N = len(strs)
        buckets = []
        table = {}
        for s in strs:
            bucket = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                bucket[index] += 1
            buckets.append(bucket)

        for i in range(N):
            bucket = tuple(buckets[i])
            if bucket not in table:
                table[bucket] = [strs[i]]
            else:
                table[bucket].append(strs[i])
        
        return list(table.values())
        
        