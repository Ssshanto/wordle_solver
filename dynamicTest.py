import algorithms

f = open('wordle-answers.txt')
words = f.read().splitlines()

unsolved = []
totalTries = 0
totalWords = 0

start = "basic"

for word in words:
	count = algorithms.dynamicSolve(f, start, word)
	totalTries += count
	totalWords += 1
	# print(word, count)
	if(count > 6):
		unsolved.append((word, count))

print("Starting wtih", start)
print(unsolved)
print(len(unsolved))
print("Average tries:", (totalTries/totalWords))


# best results with: "basic", dynamic, confidence 0.10