from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""

        for first_char in zip(*strs):
            if len(set(first_char)) == 1:
                longest_prefix += first_char[0]
            else:
                break

        return longest_prefix


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
