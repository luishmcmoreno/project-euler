file = open('0022_names.txt', 'r')
names = file.readline().split(',')
i = 1
sum_scores = 0
for name in sorted(names):
  score = 0
  for char in name:
    if (char != '"'):
      score += ord(char) - 64
  sum_scores += i * score
  i += 1
print sum_scores
