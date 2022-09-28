import math


class Solution:
    def isPalindrome(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        reverse_number = 0
        while x > reverse_number:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (reverse_number > MAX // 10 or (
                    reverse_number == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (reverse_number < MIN // 10 or (
                    reverse_number == MIN // 10 and digit <= MIN % 10)):
                return 0

            reverse_number = (reverse_number * 10) + digit

        return (reverse_number == x or x == reverse_number // 10)


if __name__ == "__main__":
    solution = Solution()

    print(solution.isPalindrome(121))
