class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        res = nums[0]

        # [3,4,5,6,9,0,1,2,3]
        while l <= r:
            # sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # rotated
            m = (l + r) // 2
            res = min(res, nums[m])
            # left portion => serach right
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
