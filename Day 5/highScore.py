# High Score
score = input().split()
for n in range(0, len(score)):
    score[n] = int(score[n])

max = 0
for i in score:
    if i > max:
        max = i

print(f"The highest score in the class is: {max}")