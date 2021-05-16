#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = True if num < 0 else False
        out = ""

        while abs(num) > 0:
            rem = abs(num) % 7
            out += str(rem)
            num = abs(num) // 7

        if neg is False:
            return out[::-1]
        else:
            return "-" + out[::-1]


# @lc code=end