from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            frequency[c].append(n)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result


if __name__ == "__main__":
    solution = Solution()

    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)

    print(result)
