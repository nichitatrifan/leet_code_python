# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

class Solution:
    def mySqrt_2(self, x: int) -> int:
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = low + (high-low)//2
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def mySqrt(self, x: int) -> int:
        val = 1
        while True:
            product = val * val
            if product == x:
                return val
            elif product > x:
                return val - 1
            else:
                val += 1

    def mySqrt_test(self, x: int) -> int:
        previous = 1
        next = 1
        found = False

        while not found:
            product = next * next
            if product == x:
                print(f"for value: {x} exact sqaure: {next}")
                previous = next
            elif product > x:
                found = True
                previous = next - 1
                print(f"for value: {x} previous: {previous}, next: {next}")
            else:
                next += 1

        return previous

if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt_2(16))