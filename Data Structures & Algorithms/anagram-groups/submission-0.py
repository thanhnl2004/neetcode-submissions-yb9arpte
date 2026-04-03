class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        table = {}
        for s in strs:
            table[s] = Counter(s)
        for s in strs:
            if not res:
                res.append([s])
            else:
                has_group = False
                for i in range(len(res)):
                    if table[res[i][0]] == table[s]:
                        res[i].append(s)
                        has_group = True
                        break
                if not has_group:
                    res.append([s])

        return res 
                

                
        
                
        