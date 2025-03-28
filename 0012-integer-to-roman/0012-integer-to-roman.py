class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        roman = []  # Store the Roman numeral result

        # Iterate through the values and subtract while adding symbols
        for value, symbol in value_to_roman:
            while num >= value:
                num -= value
                roman.append(symbol)  # Append corresponding Roman numeral

        return "".join(roman)  
        