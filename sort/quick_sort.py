import random

def quick_sort(array):
  if len(array) <= 1:
    return array

  pivot = array.pop(0)

  left, right = [], []
  for n in array:
    if n < pivot:
      left.append(n)
    else:
      right.append(n)
  
  sorted_left = quick_sort(left)
  sorted_right = quick_sort(right)

  return sorted_left + [pivot] + sorted_right

if __name__ == "__main__":
  data = list(range(10))
  rand = random.sample(data, len(data))

  print(quick_sort(rand))