# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        if len(pairs) == 0: return res
        res.append(pairs[:])
        for i in range(1, len(pairs)):
            pair = pairs[i]
            j = i - 1
            while j >= 0 and pairs[j].key > pair.key:
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = pair
            res.append(pairs[:])
        return res

        