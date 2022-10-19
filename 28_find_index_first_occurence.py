from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                match_count = 1
                for j in range(1, len(needle)):
                    if haystack[i + j] == needle[j]:
                        match_count += 1

                if match_count == len(needle):
                    return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    result = solution.strStr("a", "a")

    print(result)
