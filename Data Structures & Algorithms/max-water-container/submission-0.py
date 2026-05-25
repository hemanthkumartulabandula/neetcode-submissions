class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxarea = 0

        while left < right:

            width = right - left
            height = min(heights[left], heights[right])
            a = width * height
            if a > maxarea:
                maxarea = a
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxarea



        