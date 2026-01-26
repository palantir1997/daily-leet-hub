import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = math.inf
        second = math.inf
        for num in nums:
            if num <= first:
                first = num

            elif first <= num <= second:
                second = num
  
            else:
                return True

        return False