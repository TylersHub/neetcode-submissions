class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums != []:
            oneGreater = 1
        else:
            oneGreater = 0
        sequences = []
        nums = sorted(nums)

        for x in range(0, len(nums)-1):
            if nums[x] == nums[x + 1] - 1:
                oneGreater += 1
            else:
                if nums[x] != nums[x + 1]:
                    sequences.append(oneGreater)
                    oneGreater = 1

        sequences.append(oneGreater)

        return max(sequences)