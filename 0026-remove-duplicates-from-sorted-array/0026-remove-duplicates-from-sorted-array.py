class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        k = 1 # 처음숫자는 무조건 중복이 아니다라는 kick
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
