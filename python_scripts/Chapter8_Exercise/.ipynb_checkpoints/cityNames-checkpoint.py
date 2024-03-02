"""
Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""

def city_country(cityName, country):
    return f"{cityName}, {country}"

print(city_country("Abuja", "Nigeria"))
print(city_country("Washington D.C.", "USA"))
print(city_country("Accra", "Ghana"))