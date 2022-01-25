import algorithms

f = open('wordle-answers.txt')
words = f.read().splitlines()

unsolved = []

start = "basic"

for word in words:
	count = algorithms.dynamicSolve(f, start, word)
	# print(word, count)
	if(count > 6):
		unsolved.append((word, count))

print("Starting wtih", start)
print(unsolved)
print(len(unsolved))