freq = {} 

f = open("wordle-answers.txt", 'r')

for word in f:
	word = word.strip()
	for letter in list(set(word)):
		if letter in freq:
			freq[letter] += 1
		else:
			freq[letter] = 1


solved = False
prevWord = ""
grey = []
yellow = []
green = {}


while not solved:
	f.seek(0)
	totalP = 0

	goodness = {}
	for word in f:
		word = word.strip()
		total = 0

		good = (word != prevWord)

		for letter in grey:
			if letter in word:
				good = False

		for letter in yellow:
			if letter not in word:
				good = False

		for pos, ch in green.items():
			if word[pos] != ch:
				good = False

		if not good:
			continue;

		for letter in list(set(word)):
			total += freq[letter]

		goodness[word] = total
		totalP += total


	prevWord = (sorted(goodness.items(), key=lambda x: x[1], reverse = True)[0])[0]
	confidence = goodness[prevWord]/totalP
	print(prevWord, "\tconfidence =", confidence)

	result = input()

	if result == "22222" or result == "0":
		solved = True
		break

	if(len(result) == 5):
		for i in range(len(result)):
			if result[i] == '0':
				grey.append(prevWord[i])
			elif result[i] == '1':
				yellow.append(prevWord[i])
			else:
				green[i] = prevWord[i]

	elif(len(result) == 10):
		for i in range(0, len(result), 2):
			if result[i] == '0':
				grey.append(result[i+1])
			elif result[i] == '1':
				yellow.append(result[i+1])
			else:
				green[int(i/2)] = result[i+1]

f.close() 