from knapsack import Knapsack, Item


def print_items(bag):
  # print the total value, current capacity, and items in the bag
  print("----------------------------")
  print("total value:", bag.total_value)
  print("current capacity:", bag.current_capacity)
  print("items:")
  print("n\tv\tw")
  for i, item in enumerate(bag.items):
    print(f"{item.name}\t{item.value}\t{item.weight}")


def print_array(items):
  # print the name, value, weight, and ratio of each item in the array
  print("n\tv\tw\tr")
  for i, item in enumerate(items):
    print(f"{item.name}\t{item.value}\t{item.weight}\t{item.ratio}")
