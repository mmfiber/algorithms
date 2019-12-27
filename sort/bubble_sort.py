import random

def bubble_sort(rand):
  length = len(rand)
  # for i in range(length):
  #   for j in reversed(range(i+1, length)):
  #     if rand[j-1] > rand[j]:
  #       temp = rand[j-1]
  #       rand[j-1] = rand[j]
  #       rand[j] = temp
  i = 0
  while(length > i):
    j = length - 1
    while(j > i):
      if rand[j-1] > rand[j]:
        rand[j-1], rand[j] = rand[j], rand[j-1]
      j -= 1
    i += 1
  return rand

if __name__ == "__main__":
  data = list(range(100))
  rand = random.sample(data, len(data))

  print(bubble_sort(rand))