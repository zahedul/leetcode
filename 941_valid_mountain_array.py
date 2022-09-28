from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        length = len(arr)

        if length < 3:
            return False

        i = 1
        while i < length and arr[i] > arr[i - 1]:
            i += 1

        if i == 1 or i == length:
            return False

        while i < length and arr[i] < arr[i - 1]:
            i += 1

        return i == length


if __name__ == "__main__":
    solution = Solution()

    print(solution.validMountainArray([3, 5, 5]))
