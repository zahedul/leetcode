from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_len, word_len = 0, 0
        for i in s:
            if i == " ":
                if word_len != 0:
                    last_word_len = word_len
                word_len = 0
            else:
                word_len += 1

        return word_len if word_len != 0 else last_word_len


if __name__ == "__main__":
    solution = Solution()
    result = solution.lengthOfLastWord("   fly me   to   the moon  ")

    print(result)
