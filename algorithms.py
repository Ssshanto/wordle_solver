def basicSolve(answer, f, startingWord = ""):
	freq = {} 
	solved = False
	used = []
	grey = []
	yellow = []
	green = {}
	count = 0

	f.seek(0)

	for word in f:
		word = word.strip()
		for letter in list(set(word)):
			if letter in freq:
				freq[letter] += 1
			else:
				freq[letter] = 1


	while not solved:
		count += 1

		f.seek(0)
		totalGoodness = 0
		confidence = 0
		suggestionWord = ""
		goodness = {}

		if(startingWord == ""):
			for word in f:
				word = word.strip()
				total = 0

				good = (word not in used)

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
				totalGoodness += total
			
			suggestionWord = (sorted(goodness.items(), key=lambda x: x[1], reverse = True)[0])[0]
			confidence = goodness[suggestionWord]/totalGoodness
		else:
			suggestionWord = startingWord
			startingWord = ""
			confidence = 1
		
		
		print(suggestionWord, "\tconfidence =", confidence) 

		result = ""

		if answer != "":
			result = []

			for i in range(5):
				if suggestionWord[i] == answer[i]:
					result.append("2")
				elif suggestionWord[i] in answer:
					result.append("1")
				else:
					result.append("0")

			result = ''.join(result)

		else:
			result = input()

		if result == "22222" or result == "0":
			return count

		if(len(result) == 5):
			for i in range(len(result)):
				if result[i] == '0':
					grey.append(suggestionWord[i])
				elif result[i] == '1':
					yellow.append(suggestionWord[i])
				else:
					green[i] = suggestionWord[i]

		elif(len(result) == 10):
			for i in range(0, len(result), 2):
				if result[i] == '0':
					grey.append(result[i+1])
				elif result[i] == '1':
					yellow.append(result[i+1])
				else:
					green[int(i/2)] = result[i+1]

		used.append(suggestionWord)

def dynamicSolve(f, startingWord = "", answer = ""):
	freq = {} 
	solved = False
	used = []
	grey = []
	yellow = []
	green = {}
	count = 0
	confident = False

	f.seek(0)

	for word in f:
		word = word.strip()
		for letter in list(set(word)):
			if letter in freq:
				freq[letter] += 1
			else:
				freq[letter] = 1


	while not solved:
		count += 1

		f.seek(0)
		totalGoodness = 0
		confidence = 0
		suggestionWord = ""
		goodness = {}
		probe = {}

		good = True
		probing = True

		if(startingWord == ""):
			for word in f:
				word = word.strip()
				total = 0

				good = probing = (word not in used)

				for letter in grey:
					if letter in word:
						good = False
						probing = False

				for letter in yellow:
					if letter not in word:
						good = False
					else:
						probing = False

				for pos, ch in green.items():
					if word[pos] != ch:
						good = False
					elif letter in word:
						probing = False

				if (not good) and (not probing):
					continue;

				for letter in list(set(word)):
					total += freq[letter]

				if good:
					goodness[word] = total
					totalGoodness += total
				elif probing:
					probe[word] = total
			
			suggestionWord = (sorted(goodness.items(), key=lambda x: x[1], reverse = True)[0])[0]
			confidence = goodness[suggestionWord]/totalGoodness
			if confidence < 0.25 and len(probe) > 0:
				suggestionWord = (sorted(probe.items(), key=lambda x: x[1], reverse = True)[0])[0]
		
		else:
			suggestionWord = startingWord
			startingWord = ""
			confidence = 1
		
		# if probing:
		# 	print("Probing")

		# print(suggestionWord, "\tconfidence =", confidence) 

		result = ""

		if answer != "":
			result = []

			for i in range(5):
				if suggestionWord[i] == answer[i]:
					result.append("2")
				elif suggestionWord[i] in answer:
					result.append("1")
				else:
					result.append("0")

			result = ''.join(result)

		else:
			result = input()

		if result == "22222" or result == "0":
			return count

		if(len(result) == 5):
			for i in range(len(result)):
				if result[i] == '0':
					grey.append(suggestionWord[i])
				elif result[i] == '1':
					yellow.append(suggestionWord[i])
				else:
					green[i] = suggestionWord[i]

		elif(len(result) == 10):
			for i in range(0, len(result), 2):
				if result[i] == '0':
					grey.append(result[i+1])
				elif result[i] == '1':
					yellow.append(result[i+1])
				else:
					green[int(i/2)] = result[i+1]

		used.append(suggestionWord)


# with open('wordle-answers.txt') as f:
# 	dynamicSolve(f, "basic")
# 	f.close()
