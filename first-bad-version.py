class Solution:
    def firstBadVersion(self, n):
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l