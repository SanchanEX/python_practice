from collections import Counter

counter = Counter("フシギダネ")
print(counter)
counter.update("フシギソウ")
print(counter)
counter.update("フシギバナ")
print(counter)
print(counter.most_common(3))
