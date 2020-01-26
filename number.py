from functools import reduce

numeralMapping = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

def toArabicNumeral(romanNumeral):
  return numeralMapping.get(romanNumeral.upper())

def fromRoman(romanNumber):
  romanNumerals = list(romanNumber)
  arabicNumerals = map(toArabicNumeral, romanNumerals)
  arabicNumber = reduce(lambda prev, curr: prev + curr, arabicNumerals, 0)
  return arabicNumber

print(fromRoman('MDCLXVI')) # 1666
