def merge_sort(array, start, end):
  # Base case: if there is only one element or less in the array, return it
  if end <= start:
    return

  # Divide the array into two halves
  midpoint = (end + start) // 2
  merge_sort(array, start, midpoint)
  merge_sort(array, midpoint + 1, end)

  # Merge the two sorted halves
  merge(array, start, midpoint, end)


def merge(array, start, midpoint, end):
  left_length = midpoint - start + 1
  right_length = end - midpoint

  # Create new arrays to hold the left and right halves of the original array
  left_array = [0] * left_length
  right_array = [0] * right_length

  # Copy the left half of the original array into the left_array
  for i in range(left_length):
    left_array[i] = array[start + i]

  # Copy the right half of the original array into the right_array
  for j in range(right_length):
    right_array[j] = array[midpoint + 1 + j]

  # Merge the left and right halves into the original array
  i = j = 0
  k = start
  while i < left_length and j < right_length:
    if left_array[i].ratio > right_array[j].ratio:
      array[k] = left_array[i]
      i += 1
    else:
      array[k] = right_array[j]
      j += 1
    k += 1

  # Copy any remaining elements from the left or right halves into the original array
  while i < left_length:
    array[k] = left_array[i]
    i += 1
    k += 1

  while j < right_length:
    array[k] = right_array[j]
    j += 1
    k += 1
