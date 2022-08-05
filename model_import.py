#20220805 fabienfrfr

'''
Touseef Iqbal 2020; The survey: Text generation models in deep learning
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

path = "dataset/sherlock.txt"

with open(os.path.join(os.path.dirname(__file__), path)) as f:
	text = f.read() #see test_basic.py, text.py, splitters.py

	splitted = text.split('\n')

	#to_json = json.dumps(dict(splitted)) # test_basic.py 

'''

dlib.train_sequence_segmenter()

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