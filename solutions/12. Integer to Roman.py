class Solution:
    def intToRoman(self, num: int) -> str:
        int_mapping_list = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        res = []

        # Instead of while + break, iterate through the list once
        for val, roman in int_mapping_list:
            # If num becomes 0, we can stop early
            if num == 0:
                break

            # Use divmod to get count and remainder for efficiency
            # Or a simple while loop here to subtract multiple same values
            while val <= num:
                num -= val
                res.append(roman)

            # count, num = divmod(num, val)
            # if count > 0:
            #     res.append(roman * count)

        return ''.join(res)
