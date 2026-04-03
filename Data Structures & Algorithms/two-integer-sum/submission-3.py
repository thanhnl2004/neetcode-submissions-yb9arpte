class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        res = [-1, -1]
        for i in range(len(nums)):
            if target - nums[i] not in table:
                table[nums[i]] = i
            else:
                res[0] = table[target - nums[i]]
                res[1] = i
                break
        
        return res
        
        