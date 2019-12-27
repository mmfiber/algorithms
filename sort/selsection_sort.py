import random

def selection_sort(rand):
  length = len(rand)
  # for i in range(length):
  #   min_idx = i
  #   for j in range(i+1, length):
  #     if rand[j] < rand[min_idx]:
  #       min_idx = j
  #   rand[min_idx], rand[i] = rand[i], rand[min_idx]
  i = 0
  while(i < length):
    min_idx = i
    j = i
    while(j < length):
      if rand[j] < rand[min_idx]:
        min_idx = j
      j += 1
    rand[min_idx], rand[i] = rand[i], rand[min_idx]
    i += 1
  return rand

if __name__ == "__main__":
  data = list(range(100))
  rand = random.sample(data, len(data))

  print(selection_sort(rand))