class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #          1 2 4 6
        # prefix:  1 1 2 8 
        # suffix: 48 24 6 1
        res = [1] * len(nums)
        left, right = 1, 1

        for i in range(1, len(nums)):
            left *= nums[i - 1]
            res[i] = left

        for i in range(len(nums) - 2, -1 , -1):
            right *= nums[i + 1]
            res[i] *= right

        return res
        
        


        