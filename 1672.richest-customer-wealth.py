#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        balances = []

        for customer in accounts:
            sum = 0
            for bank_bal in customer:
                sum += bank_bal
            balances.append(sum)

        return max(balances)


# @lc code=end