import random

def merge_sort(array):
  if len(array) == 1:
    return array

  mid_idx = len(array) // 2
  left = merge_sort(array[:mid_idx])
  right = merge_sort(array[mid_idx:])

  return merge(left, right)

def merge(left, right):
  lst = []
  while(left or right):
    if left and right:
      add = left.pop(0) if left[0] < right[0] else right.pop(0)
    elif not left:
      add = right.pop(0)
    elif not right:
      add = left.pop(0)
    lst.append(add)
  return lst

if __name__ == "__main__":
  data = list(range(100))
  rand = random.sample(data, len(data))

  print(merge_sort(rand))