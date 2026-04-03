class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            # sorted array
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # rotated
            m = (l + r) // 2
            res = min(res, nums[m])
            # left portion => search right
            if nums[m] >= nums[l]:
                l += 1
            else:
                 r -= 1
        
        return res

        