class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        low = 0
        high = x
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid     
                low = mid + 1
            else:
                high = mid - 1

        return result
        
