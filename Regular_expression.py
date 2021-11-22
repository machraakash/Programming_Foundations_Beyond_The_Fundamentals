import re

five_letter_names = 'roman'
six_letter_names = 'fulhem'
four_letter_names = 'weh'

find_range = r'\w{5,6}'
print(re.search(find_range, five_letter_names))
print(re.search(find_range, six_letter_names))
print(re.search(find_range, four_letter_names))