class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left_v = 1
        right_v = 1

        for i in range(n):
            ans[i] *= left_v
            left_v *= nums[i]

            j = n - 1 - i
            ans[j] *= right_v
            right_v *= nums[j]

        return ans
        