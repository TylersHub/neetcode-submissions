class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return nums
            
        nums = sorted(nums)
        num_lists = []

        list_start = 0
        for x in range(1, len(nums)):
            if x == len(nums)-1:
                if nums[x-1] != nums[x]:
                    num_lists.append([nums[x]])
                else:
                    num_lists.append(nums[list_start:x+1])
            if nums[x-1] != nums[x]:
                num_lists.append((nums[list_start:x]))
                list_start = x

        num_lists = sorted(num_lists, key=len, reverse=True)
        
        return [x[0] for x in num_lists[0:k]]

