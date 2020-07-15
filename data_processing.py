
def make_array(txt):
	"""
	takes in the txt and returns a vector of the whole text with single words
	also returns a dict of all words with frequencies
	"""
	import string
	sequence = []
	dow = {} 	# dict of words
	with open(txt,'r') as f:
		for line in f:
			for word in line.split():
				word = word.translate(str.maketrans('', '', string.punctuation))
				word = word.lower()
				sequence.append(word)
				if word in dow:
					dow[word] += 1
				else:
					dow[word] = 1
	return sequence, dow

def syllabise(word):
	"""
	return the number of syllables in a word
	"""
	syllables = 0
	i_factor = False
	huj = ['a','ą','e','ę','o','ó','u','y']
	for i in word:
		if i in huj:
			syllables += 1
			i_factor = False
		elif i == 'i' and word != 'i':
			i_factor = True
		elif len(word) == 1:
			syllables = 1
		elif i not in huj and i_factor == True:
			syllables += 1
		else:
			pass
	return syllables

def random_haiku(sequence):
	"""
	based on probabilities alone make a haiku
	"""
	import random
	haiku = [[],[],[]]
	for i,line in enumerate(haiku):
		if i == 1:
			l = 7
		else:
			l = 5
		
		while l != 0:
			x = random.randint(0,len(sequence)-1)
			word = sequence[x]
			#print(word)
			#print(type(word))
			w = syllabise(word)	
			haiku[i].append(word)
			l -= w
			if l < 0:
				if i == 1:
					l = 7 - w
				else:
					l = 5 - w
				haiku[i] = [word]
			#print(haiku)
			#print(f"l: {l}")
			#input()
	return haiku
	print(haiku)
		

def bigram_haiku_data(sequence, dow):
	"""
	based on an array of frequencies make a haiku
	"""
	import random
	import numpy as np

	words = []
	for key in dow:
		words.append(key)
	words = sorted(words)
	fq = np.zeros((len(words),len(words)))
	for i in range(len(sequence)-1):
		cw = words.index(sequence[i])
		w1 = words.index(sequence[i+1])
		fq[cw,w1] += 1
	weights = []
	for word in words:
		weights.append(dow[word])
	return fq, words, weights


def bigram_haiku(fq, words, weights):
	"""
	generate from data and word list
	"""
	import random
	haiku = [[],[],[]]
	for i,line in enumerate(haiku):
		if i == 1:
			l = 7
		else:
			l = 5
		
		while l != 0:
			word = random.choices(words, weights=weights, k=1)[0]
			#print(word)
			#print(type(word))
			w = syllabise(word)	
			haiku[i].append(word)
			l -= w
			while l != 0:
				cw = words.index(word)
				word = random.choices(words, weights=fq[cw,:], k=1)[0]
				w = syllabise(word)
				l -= w
				haiku[i].append(word)
				if l < 0 or l == 1:
					if i == 1:
						l = 7
					else:
						l = 5
					haiku[i] = []
					break	
			
	return haiku
	print(haiku)


def check_rhyme(word1, word2):
	"""
	checks if word1 and word2 rhyme
	"""
	smol = min(len(word1),len(word2), 4)
	
	if word1[-smol:] == word2[-smol:]:
		return True
	else:
		return False




def bigram_hot16(fq, words, weights):
	"""
	generate from data and word list
	think about rhymes
	"""
	import random
	hot16 = [[] for _ in range(16)]
	for i, line in enumerate(hot16):
		l = random.randint(8,12)
		while l != 0:
			word = random.choices(words, weights=weights, k=1)[0]
			#print(word)
			#print(type(word))
			w = syllabise(word)	
			hot16[i].append(word)
			l -= w
			while l != 0:
				cw = words.index(word)
				word = random.choices(words, weights=fq[cw,:], k=1)[0]
				w = syllabise(word)
				l -= w
				hot16[i].append(word)
				if l < 0 or l == 1:
					l = random.randint(8,12)
					hot16[i] = []
					break	
		
	
	return hot16


