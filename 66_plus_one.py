from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        added_list = []
        add_value = 1
        for i in range(len(digits)-1, -1, -1):
            value = add_value + digits[i]
            added_list.append(value % 10)
            add_value = value // 10

        if add_value == 1:
            added_list.append(add_value)

        return list(reversed(added_list))

    def plusOneAlernative(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            if len(digits) == 1:  # Already a 9
                return [1, 0]
            return self.plusOneAlernative(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9]))
    print(solution.plusOne([4, 3, 2, 1]))
    print(solution.plusOne([1, 2, 3]))

