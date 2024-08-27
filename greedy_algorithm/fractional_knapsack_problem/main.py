from sort import merge_sort
from knapSack import Knapsack, Item
from prints import print_array, print_items

# create arrays of randomly assigned values and weights
values = [4, 9, 12, 11, 6, 5]
weights = [1, 2, 10, 4, 3, 5]

# Creating an array of Item objects
items = []
array_length = len(values)

for i in range(len(values)):
  new_item = Item(values[i], weights[i], "#" + str(i))
  items.append(new_item)

# Sorting the array of Item objects based on the ratio of value to weight
merge_sort(items, 0, len(items) - 1)

# Printing the sorted array of Item objects
print_array(items)

# Creating a Knapsack object and adding items to it until its current capacity reaches its maximum capacity
j = 0
bag = Knapsack(12)
while bag.current_capacity < bag.max_capacity:
  bag.add_item(items[j])
  j += 1

# Printing the items in the Knapsack object
print_items(bag)
