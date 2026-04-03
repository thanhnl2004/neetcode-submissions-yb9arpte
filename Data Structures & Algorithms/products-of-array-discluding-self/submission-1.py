class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,1,2,8] L
        # [48,24,6,1] R
        res = [1 for _ in nums]
        left = 1
        for i in range(1, len(nums)):
            left *= nums[i - 1]
            res[i] = left
        
        right = 1
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            res[i] *= right

        return res