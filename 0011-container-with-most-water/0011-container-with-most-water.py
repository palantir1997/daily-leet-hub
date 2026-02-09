class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            # 현재 가로 길이 계산 ex) 8, 7, 6
            width = right - left

            # 현재 세로 길이 중 (둘 중 더 낮은 벽) 결정 및 넓이 계산 ex) 1 7 3
            current_height = min(height[left], height[right])
            current_water = width * current_height # ex) 8 49 18

            # 최대 길이 업데이트 ex) 8,49, 
            max_water = max(max_water, current_water)

            if height[left] < height[right]:
                left += 1 # left = 1
            else:
                right -= 1 # right = 7
        return max_water
            