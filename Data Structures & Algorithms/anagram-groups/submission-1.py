class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket_list = []
        table = {}
        for s in strs:
            bucket = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                bucket[index] += 1
            bucket_list.append(tuple(bucket))

        for i in range(len(bucket_list)):
            bucket = bucket_list[i]
            if not table or bucket not in table:
                table[bucket] = [strs[i]]
            else:
                table[bucket].append(strs[i])

        return list(table.values())
                
                

        

        