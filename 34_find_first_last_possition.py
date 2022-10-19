from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int, left_biased: bool) -> int:
        l, r = 0, len(nums) - 1
        index = -1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                index = m
                if left_biased:
                    r = m - 1
                else:
                    l = m + 1

        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)

        return [left, right]


if __name__ == "__main__":
    solution = Solution()
    result = solution.searchRange([5, 7, 7, 8, 8, 10], 8)

    print(result)
