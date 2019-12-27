import random

def insertion_sort(rand):
  length = len(rand)
  # for i in range(1, length):
  #   for j in reversed(range(i)):
  #     if rand [j] > rand[j+1]:
  #       rand[j], rand[j+1] = rand[j+1], rand[j]
  #     else:
  #       break
  i = 1
  while(length > i):
    j = i
    while(j > 0):
      if rand[j] < rand[j-1]:
        rand[j-1], rand[j] = rand[j], rand[j-1]
        j -= 1
      else:
        break
    i += 1
  return rand

if __name__ == "__main__":
  data = list(range(100))
  rand = random.sample(data, len(data))

  print(insertion_sort(rand))