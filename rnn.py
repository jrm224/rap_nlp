import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
def prepare(txt, n_words):
	"""
	a function to tokenize .txt
	requires tf and tokenize
	"""
	file = open(txt)
	text = file.read().split('\n')
	text = text
	tokenizer = Tokenizer(num_words=n_words, filters='\n')
	tokenizer.fit_on_texts(text)
	sequences = tokenizer.texts_to_sequences(text)
	
	return sequences, tokenizer, text

def create_input_sequences(sequences):
	"""
	create a list of input sequences for each sequence
	"""
	input_sequences = []
	for s in sequences:
		for i in range(1, len(s)):
			n_gram_sequence = s[:i+1]
			input_sequences.append(n_gram_sequence)
	input_sequences = pad_sequences(input_sequences, padding='pre')
	return input_sequences

def generate_training_set(i_s, n_words):
	"""
	based on a set of input sequences we generate xs and labels
	"""
	x = i_s[:,:-1]
	y = i_s[:,-1]
	y = tf.keras.utils.to_categorical(y, num_classes=n_words)
	return x, y

def setup_model(n_words, l):
	"""
	takes in the number of words and length of the sequence
	set up the model for nn
	"""
	model = Sequential()
	model.add(Embedding(n_words, 100, input_length=l))
	model.add(Bidirectional(LSTM(150)))
	model.add(Dense(n_words, activation='softmax'))
	
	return model

def setup_compilation(model, x, y):
	"""
	proxy for setting up the compilation properly
	"""
	adam = Adam(lr=0.01)
	model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
	history = model.fit(x, y, epochs=10, verbose=1)
	
	return history
