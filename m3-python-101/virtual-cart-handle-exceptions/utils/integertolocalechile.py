import re
def format_currency(amount):
    return re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"${amount}")
"""
r'(?<!^)(?=(\d{3})+$)'
1. (?<!^)
This is a negative lookbehind assertion.
It ensures that the position is not at the start of the string.
This prevents the regex from matching at the beginning of the string.

2. (?=(\d{3})+$)
This is a positive lookahead assertion.
It checks that the position is followed by one or more groups
of exactly three digits until the end of the string.

3. \d{3}
Matches exactly three digits.

3.1 (\d{3})+
Matches one or more groups of three digits.

4. $
Asserts the position at the end of the string.

In summary, this regex matches positions in the string
where there are groups of three digits to the right,
but not at the start of the string. This is used to insert a period .
as a thousands separator in the currency format.
"""