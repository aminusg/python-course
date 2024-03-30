"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""
import math


sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

my_list = sorted(sale_prices)
print(my_list)

number_of_sales = len(my_list)
first_sales_items = my_list[:math.floor(number_of_sales/2)]


#Solution:
sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)
