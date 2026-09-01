class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= 1:
            return nums

        k_arr = []
        key_arr = []
        unique_elements = {}

        for num in nums:
            try:
                if unique_elements[num]:
                    unique_elements[num] += 1
            except:
                unique_elements[num] = 1

        print("original: " + str(unique_elements))

        #sorted(unique_elements.values())
        sorted_by_values = dict(sorted(unique_elements.items(), key = lambda item: item[1]))

        print("sorted: " + str(sorted_by_values))

        tot = len(sorted_by_values) - k
        itr = 0

        for key in sorted_by_values.keys():
            key_arr.append(key)

        for key in key_arr:
            try:
                if itr < tot:
                    sorted_by_values.pop(key, None)
                    itr += 1
            except:
                continue

        print("final dict: " + str(sorted_by_values))


        # Find a way to iterate through minimum values until lenth - k
    

        for key in sorted_by_values:
            k_arr.append(key)

        print("final k_arr: " + str(k_arr))

        return k_arr