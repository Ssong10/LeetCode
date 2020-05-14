class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        no_rob = [0] * len(nums)
        rob = [0] * len(nums)
        for i in range(len(nums)):
            no_rob[i] = rob[i-2] + nums[i]
            rob[i] = max(no_rob[i-1],rob[i-2]) + nums[i]
        print(no_rob, rob)
        return max(rob)