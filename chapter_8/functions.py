# parameter 1: accept list  of items a person wants on sandwhich
# print summary of sandwhich status ordered, print 3 times
def samich_toppings(username, toppings):
  print("==========================\n")
  print(f"{username} wants...\n")
  for topping in toppings:
    print(f"{topping}!")
  print("\n\n")

samich_toppings('myusername', [
  'salami',
  'pickles',
  'cheese'])

samich_toppings("dfuentes",[
  'topin1',
  '2',
  'pepperoni'
])


samich_toppings(toppings=[
  'mytoping',
  'another',
  '!!@OI#U@O#!@#OIU'
], username="edgars")

# SIMPLE DATA TYPE --------
# String - collections inside quotations
# "asdfkjadsflk "
# Number 
# 12332423
# # List - collection of same data types, in brackets [] seperated by ,
# ['asdf', 'asdf', 'asdf']
# [
#   'asdf',
#   'asdf', 
#   'asdf'
# ]
# # list of numbers
# [3, 4, 4]
# # Dictionary - collection of key value pairs
# # value can be any data type
# { 
#   'mykey': 2,
#   'treds': '234'
# }
# END: SIMPLE DATA TYPE --------

