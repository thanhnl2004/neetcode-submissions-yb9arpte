class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            if target - nums[i] not in table:
                table[nums[i]] = i
            else:
                smallerIndex = min(i, table[target - nums[i]])
                largerIndex = max(i, table[target - nums[i]])

                return [smallerIndex, largerIndex]

        return []
        