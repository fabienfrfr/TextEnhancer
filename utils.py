# 20220806 fabienfrfr

import re, dlib

######### SPLIT FUNCTION
initialism_pat = re.compile(r"^[A-Za-z0-9]{1,2}(\.[A-Za-z0-9]{1,2})+\.$", re.UNICODE)

def is_sentence_ender(word):
	if re.match(initialism_pat, word) is not None:
		return False
	if word[-1] in ["?", "!"]:
		return True
	if len(re.sub(r"[^A-Z]", "", word)) > 1:
		return True
	if word[-1] == "." :
		return True
	return False

def split_into_sentences(text):
	potential_end_pat = re.compile(
		r"".join([ 	r"([\w\.'’&\]\)]+[\.\?!])",  # A word that ends with punctuation
					r"([‘’“”'\"\)\]]*)",  # Followed by optional quote/parens/etc
					r"(\s+(?![a-z\-–—]))",  # Followed by whitespace + non-(lowercase/dash)
			]), re.U,)

	dot_iter = re.finditer(potential_end_pat, text)
	end_indices = [	(x.start() + len(x.group(1)) + len(x.group(2)))
					for x in dot_iter if is_sentence_ender(x.group(1))]
	spans = zip([None] + end_indices, end_indices + [None])
	sentences = [text[start:end].strip().replace('\n',' ') for start, end in spans]

	return sentences

###### VECTORIZE FUNCTION

def sentence_to_vectors(sentence):
	# Create an empty array of vectors
	vects = dlib.vectors()
	for word in sentence.split():
		# Our vectors are very simple 1-dimensional vectors.  The value of the
		# single feature is 1 if the first letter of the word is capitalized and
		# 0 otherwise.
		if word[0].isupper():
			vects.append(dlib.vector([1]))
		else:
			vects.append(dlib.vector([0]))
	return vects
