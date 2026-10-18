import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
  """
  Generates a set of random unique numbers within the given parameters.

  :param min: min possible number, cannot be less than 1
  :param max: max possible number, cannot be more than 1000
  :param quantity: the amount of numbers to be chosen between `min` and `max` values,
           if less than 1 an empty array returns

  :return: a set of random unique numbers within the given parameters
           or an empty array if the parameters are not met.
  """

  not_satisfies_min = min < 1 or min > max
  not_satisfies_max = max > 1000
  not_satisfies_quantity = quantity < 1 or quantity > max - min + 1

  if (not_satisfies_min or not_satisfies_max or not_satisfies_quantity):
    return []

  numbers_set = range(min, max + 1)
  selection = sorted(random.sample(numbers_set, quantity))

  return selection


# print('Your lottery numbers:', get_numbers_ticket(1, 49, 6)) # Every run returns a new set of 6 unique numbers
# print('Your lottery numbers:', get_numbers_ticket(50, 49, 6)) # Returns an empty array
# print('Your lottery numbers:', get_numbers_ticket(-1, 49, 6)) # Returns an empty array
# print('Your lottery numbers:', get_numbers_ticket(1, 1001, 6)) # Returns an empty array
# print('Your lottery numbers:', get_numbers_ticket(1, 6, 6)) # Returns an empty array