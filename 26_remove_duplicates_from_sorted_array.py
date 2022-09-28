from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pos = 0
        for i in range(1, len(nums)):
            if nums[pos] != nums[i]:
                nums[pos + 1] = nums[i]
                pos += 1

        return pos + 1


if __name__ == "__main__":
    solution = Solution()

    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
