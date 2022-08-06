# 20220805 fabienfrfr

'''
Touseef Iqbal 2020; The survey: Text generation models in deep learning

WORK IN PROGESS
https://www.kdnuggets.com/2020/01/guide-natural-language-generation.html https://www.youtube.com/watch?v=dT1aKuUsKUE
USING MARKOV CHAIN STRUCTURED GRAPH & LSTM (simple model)

https://github.com/davisking/dlib/blob/master/python_examples/sequence_segmenter.py
https://github.com/jsvine/markovify #for some inspiration
http://scikit-learn.sourceforge.net/stable/modules/hmm.html
https://www.kdnuggets.com/2020/07/pytorch-lstm-text-generation-tutorial.html
https://www.kaggle.com/code/ab971631/beginners-guide-to-text-generation-pytorch/notebook
'''

import re, os
import dlib, torch
import json

from utils import split_into_sentences, sentence_to_vectors

path = "dataset/sherlock.txt"


with open(os.path.join(os.path.dirname(__file__), path)) as f:
	text = f.read()

sentences = split_into_sentences(text)
# Make an array of arrays of dlib.vector objects.
training_sequences = dlib.vectorss()
for s in sentences :
	training_sequences.append(sentence_to_vectors(s))
# init train
params = dlib.segmenter_params()
params.window_size = 3
params.use_high_order_features = True
params.use_BIO_model = True
# common SVM parameter
params.C = 10
# Train a model Monte Carlo Markov Chain
model = dlib.train_sequence_segmenter(training_sequences, sentences, params) # overloaded function
for i, s in enumerate(sentences):
	print(model(training_sequences[i]))
# save markov chain model
#to_json = json.dumps(dict(splitted)) # test_basic.py 

'''

"""
Goal : Train 2 type of model, first Markov Chain (without markovify module, here with dlib), and the second, with LSTM seq2seq.

"""

from torch import nn

class Model(nn.Module):
	def __init__(self, dataset):
		super(Model, self).__init__()
		self.lstm_size = 128
		self.embedding_dim = 128
		self.num_layers = 3

		n_vocab = len(dataset.uniq_words)
		self.embedding = nn.Embedding(
			num_embeddings=n_vocab,
			embedding_dim=self.embedding_dim,
		)
		self.lstm = nn.LSTM(
			input_size=self.lstm_size,
			hidden_size=self.lstm_size,
			num_layers=self.num_layers,
			dropout=0.2,
		)
		self.fc = nn.Linear(self.lstm_size, n_vocab)

	def forward(self, x, prev_state):
		embed = self.embedding(x)
		output, state = self.lstm(embed, prev_state)
		logits = self.fc(output)
		return logits, state

	def init_state(self, sequence_length):
		return (torch.zeros(self.num_layers, sequence_length, self.lstm_size),
				torch.zeros(self.num_layers, sequence_length, self.lstm_size))

'''