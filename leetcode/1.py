class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            search_num = target - num
            if search_num not in hashmap:
                hashmap[num] = i
            else:
                return [i, hashmap[search_num]]
