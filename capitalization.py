first_name = 'parul'
second_name = 'chandrika'
designation = 'savior of the family'

first_name_cap = first_name.capitalize()
second_name_cap = second_name.capitalize()

print(first_name_cap, second_name_cap, 'is the', designation)

location_family = designation.index('the')
print(location_family)

reverse_location_family = designation.rfind('the')
print(reverse_location_family)

string_slice = designation[10:]
print(string_slice)