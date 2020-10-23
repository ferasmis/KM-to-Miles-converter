
## Author: Feras
## Description: Kilometers to Miles distance converter
## Formula: Miles = Kilometers / 1.61 where 1.61 Km = 1 mi

print('Hello, this is a KM to Miles calculator. \
 Please enter the distance as a decimal number for example  12.1 or 8')

km = float(input('Please enter the distance in KM: \n KM '))
converter = 1.61
miles = km / converter
print('The distance in Miles: ', miles)
