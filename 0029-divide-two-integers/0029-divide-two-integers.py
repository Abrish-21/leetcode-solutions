class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # Prevent overflow
        
        # Determine the sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # Bitwise division using left shift
        while a >= b:
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple
        
        # Apply sign
        return max(INT_MIN, min(INT_MAX, quotient * sign))
        