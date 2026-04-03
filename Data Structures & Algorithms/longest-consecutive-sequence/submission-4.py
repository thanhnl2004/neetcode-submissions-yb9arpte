class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,3,4,4,5,...10....20]
        se = set(nums)
        maxLens = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            n = nums[i]
            # if have left neighour => not start of sequence
            if n - 1 in se:
                continue
            # start of sequence => find max possible consecutive sequence
            else:
                while n + 1 in se:
                    maxLens[i] += 1
                    n += 1

        if not maxLens:
            return 0
        else:
            return max(maxLens)
            
