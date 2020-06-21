class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        no_rob = [0] * len(nums)
        rob = [0] * len(nums)
        for i in range(len(nums)):
            no_rob[i] = max(rob[i-1], no_rob[i-2]+nums[i])
            rob[i] = max(no_rob[i-2],rob[i-2]) + nums[i]
        return max(rob[-2:])