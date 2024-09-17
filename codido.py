def roman_to_int(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10}
    total = 0
    for char in roman:
        total += roman_values.get(char, 0)
    return total