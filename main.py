# fabienfrfr 20220712
# Import package
import os, argparse
import openai
import numpy as np, pandas as pd
from tqdm import tqdm

## Decouple environment
from decouple import config
os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')
#keys = [k for k in os.environ if("OPENAI" in k)]
#API gpt3
openai.api_key = os.getenv("OPENAI_API_KEY")

## Input
parser = argparse.ArgumentParser(description='Improve an academic thesis in one click? - App using GPT-3 API')
parser.add_argument('-i', '--input', type=str, required=False, help='directory of input dissertation text file')

## Path
INPUT_FILE = "INPUT.txt"
OUTPUT_FILE = "OUTPUT.csv"

## function
def simplify_input_text(path) :
	f = open(path, "r")
	untaken = ['\ufeff\n', '\n']
	texts = []
	# using "readline" rather then "readlines" for long file input
	while True:
		line = f.readline()
		if not(line) : break
		else :
			boolean = np.sum([line == u for u in untaken])
			if boolean == 0 :
				texts += [line]
	df = pd.DataFrame(texts, columns=['section'])
	df['line'] = df.index
	return df[['line','section']]

def RearrangeTextData(df):
	#table = df.section.str.split(".", expand=True).fillna('')
	table = df.section.apply(lambda x:x.split('.')).apply(pd.Series).fillna('')
	df = pd.concat((texts, table), axis=1)
	# replace
	df.replace('\n', '', inplace=True)
	df.replace(' \n', '', inplace=True)
	return df

def gpt3_completion(df) :
	for index, row in tqdm(df.iterrows(), total=df.shape[0]):
		for col, value in row.iteritems() :
			if value != '' :
				## gpt-3
				response = openai.Completion.create(
					model="text-davinci-002", 
					prompt="Améliore en Français : " + value, 
					temperature=0.7, 
					max_tokens=2048)
				# extract text
				new_text = response["choices"][0]["text"]
				df.loc[index, col] = new_text

## run
if __name__ == '__main__':
	args = parser.parse_args()
	## Apply
	print('[INFO] Starting System')
	if args.input == None :
		path = INPUT_FILE
	else :
		path = args.input
	print('[INFO] Extract text and simplify')
	texts = simplify_input_text(path)
	print('[INFO] Rearrange the dataframe')
	texts = RearrangeTextData(texts)
	print('[INFO] Completion of each texts')
	new_texts = texts.copy()
	new_texts.pop('line')
	## NEED TO IMPROVE : save checkpoint if quota exceed
	gpt3_completion(new_texts)
	print('[INFO] Save to csv')
	new_texts.to_csv(OUTPUT_FILE, sep=';', index=False)