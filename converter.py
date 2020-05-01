numeral_mapping = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

to_arabic_numeral = lambda roman_numeral: numeral_mapping.get(roman_numeral.upper())

def summerize(arabic_numerals):
  if len(arabic_numerals) == 1:
    return arabic_numerals[0]

  sum = 0
  for numeral_1, numeral_2 in zip(arabic_numerals, arabic_numerals[1:]):
    if numeral_1 < numeral_2:
      sum += -1 * numeral_1
    else:
      sum += numeral_1
  return sum + arabic_numerals[-1]

def from_roman(roman_numerals):
  arabic_numerals = list(map(to_arabic_numeral, roman_numerals))
  arabic_number = summerize(arabic_numerals)
  return arabic_number

print(from_roman('MDCLXVI')) # 1666
print(from_roman('XIV')) # 14
print(from_roman('IV')) # 4
