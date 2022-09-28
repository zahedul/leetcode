class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")

        total_sum = 0
        for i in s:
            total_sum += dictionary[i]

        return total_sum


if __name__ == "__main__":
    solution = Solution()

    print(solution.romanToInt("LVIII"))
