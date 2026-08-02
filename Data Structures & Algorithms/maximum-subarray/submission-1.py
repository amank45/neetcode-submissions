class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        mx = nums[0]

        for i in nums:
            if count < 0:
                count = 0
            count += i
            mx = max(count,mx)

        return mx  

        