from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_array = {}
        for i in range(len(nums)):
            if nums[i] in duplicate_array and (i - duplicate_array[nums[i]]) <= k:
                return True

            duplicate_array[nums[i]] = i

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
