class RomanNumerals:
    mapper = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
    @classmethod
    def to_roman(cls,val: int) -> str:
        roman_str = ""
        for key in sorted(cls.mapper.keys(), reverse=True):
            while val >= key:
                roman_str += cls.mapper[key]
                val -= key
        return roman_str

    @classmethod
    def from_roman(cls,roman_str: str) -> int:
        roman_int = 0
        for k,v in cls.mapper.items():
            if len(v) < 2:
                continue
            if v in roman_str:
                roman_int += k
                roman_str = roman_str.replace(v, "")

        for k,v in cls.mapper.items():
            while v in roman_str:
                roman_int += k
                roman_str = roman_str.replace(v, "",1)

        return roman_int

# print(RomanNumerals.to_roman(1989))
print(RomanNumerals.to_roman())
