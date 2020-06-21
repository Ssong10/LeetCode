class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = {}
        for num in nums:
            if num in numbers:
                del numbers[num]
            else:
                numbers[num] = 1
        for key in numbers:
            return key