from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0

        while left < right:
            new_area = (right - left) * min(height[left], height[right])
            area = max(area, new_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxArea([1, 2, 3, 4, 5, 6, 7]))
