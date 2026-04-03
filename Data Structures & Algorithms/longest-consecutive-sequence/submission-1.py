class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se = set(nums)
        lcs = [0 for _ in range(len(nums))]

        if len(nums) == 0: return 0

        for i in range(len(nums)):
            num = nums[i]
            if num - 1 in se:
                continue
            else:
                lcs[i] = 1
                nextNum = num + 1
                while nextNum in se:
                    lcs[i] += 1
                    nextNum += 1

        return max(lcs)


        