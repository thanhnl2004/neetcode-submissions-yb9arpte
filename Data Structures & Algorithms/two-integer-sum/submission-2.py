class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        res = []
        for i in range(len(nums)):
            if len(table) == 0 or target - nums[i] not in table:
                table[nums[i]] = i
            else:
                res.append(table[target-nums[i]])
                res.append(i)
                break
        
        return res
    
                


        