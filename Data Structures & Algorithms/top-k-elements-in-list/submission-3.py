class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, f in freq.items():
            bucket[f].append(num)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            vals = bucket[i]
            for val in vals:
                if len(res) == k:
                    break
                else:
                    res.append(val)

        return res

        