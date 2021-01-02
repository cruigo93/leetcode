from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 1:
            return False
        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid * mid < num:
                low = mid + 1
            if mid * mid > num:
                high = mid - 1
            if mid * mid == num:
                return True
        # print(mid, low, high)
        return False


def main():
    s = Solution()
    num = 82
    print(s.isPerfectSquare(num))


if __name__ == "__main__":
    main()