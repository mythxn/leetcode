#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        w = l = r = 0

        for i in s:
            if i == "L":
                l += 1
            elif i == "R":
                r += 1
                
            if l == r:
                w += 1
        return w


# @lc code=end
