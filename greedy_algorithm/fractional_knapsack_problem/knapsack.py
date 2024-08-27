class Knapsack:
  # initialize the knapsack properties
  def __init__(self, max_capacity):
    self.max_capacity = max_capacity
    self.current_capacity = 0
    self.total_value = 0
    self.items = []

  # add an item to the knapsack
  def add_item(self, new_item):
    # if the item is too heavy, adjust its weight and value
    if new_item.weight > self.max_capacity - self.current_capacity:
      diff = self.max_capacity - self.current_capacity
      new_item.weight = diff
      new_item.value = diff * new_item.ratio

    # add the item to the knapsack and update its properties
    self.items.append(new_item)
    self.current_capacity += new_item.weight
    self.total_value += new_item.value


class Item:
  # initialize the item properties and calculate its ratio
  def __init__(self, value, weight, name):
    self.value = value
    self.weight = weight
    self.name = name
    self.ratio = value / weight if weight != 0 else 0
