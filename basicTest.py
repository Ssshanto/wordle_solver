import algorithms

f = open('wordle-answers.txt')
words = f.read().splitlines()

start = "basic"

unsolved = []

for word in words:
	count = algorithms.basicSolve(f, start, word)
	# print(word, count)
	if(count > 6):
		unsolved.append((word, count))

print("Starting wtih", start)
print(unsolved)
print(len(unsolved))

# best = ""
# bestLen = 3500
# bestUnsolved = []

# for start in words:
# 	unsolved = []

# 	for word in words:
# 		count = algorithms.basicSolve(f, start, word)
# 		# print(word, count)
# 		if(count > 6):
# 			unsolved.append((word, count))

# 	if(len(unsolved) < bestLen):
# 		bestLen = len(unsolved)
# 		best = start
# 		bestUnsolved = unsolved

# 	print("Starting wtih", start)
# 	print(len(unsolved))
# 	print("Current best", bestLen)

# print(best, bestUnsolved, bestLen)

# best = basic, bestLen = 48





	



