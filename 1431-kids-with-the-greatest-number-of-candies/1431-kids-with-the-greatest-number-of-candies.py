class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxval = max(candies)
        list = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxval:
                list.append(True)
            else:
                list.append(False)
        return list
