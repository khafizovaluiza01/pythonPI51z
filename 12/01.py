text = input()
words = text.split()

result = []
for i in range(2, len(words), 3):
    result.append(words[i])

print(*result)