class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            for y in range(x, len(nums)):
                if nums[x] == nums[y] and x != y:
                    return True
        return False
         