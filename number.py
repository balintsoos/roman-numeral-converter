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

def summerize(arabicNumerals):
  sum = 0
  for previous, current in zip(arabicNumerals, arabicNumerals[1:]):
    if previous < current:
      sum += (-1 * current)
    else:
      sum += current
  return sum

def fromRoman(romanNumber):
  romanNumerals = list(romanNumber)
  arabicNumerals = map(toArabicNumeral, romanNumerals)
  arabicNumber = summerize(list(arabicNumerals))
  return arabicNumber

# print(fromRoman('MDCLXVI')) # 1666
print(fromRoman('XIV'))

