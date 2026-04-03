class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = [[0] * 26 for _ in strs]
        table =  {}
        for i in range(len(strs)):
            bucket = buckets[i]
            s = strs[i]
            for c in s:
                index = ord(c) - ord('a')
                bucket[index] += 1
        for i in range(len(strs)):
            bucket = tuple(buckets[i]) # convert to tuple to hash
            s = strs[i]
            if bucket not in table:
                table[bucket] = [s] 
            else:
                table[bucket].append(s)           

        return list(table.values())
        