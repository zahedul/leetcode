from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        heavy_person = len(people) - 1
        light_person = 0

        boats = 0

        while heavy_person >= light_person:
            if heavy_person == light_person:
                boats += 1
                break

            if people[heavy_person] + people[light_person] <= limit:
                light_person += 1

            boats += 1
            heavy_person -= 1

        return boats


if __name__ == "__main__":
    solution = Solution()

    print(solution.numRescueBoats([3, 5, 3, 4], 5))
