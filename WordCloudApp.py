import pandas as pd
from textblob import Word, TextBlob
import string
import re
from nltk.corpus import stopwords
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import streamlit as st
import time
import nltk

nltk.download('stopwords')
os.system('python -m spacy download en_core_web_sm')

def clean(text):

	#Remove emojis and special elements
	text = text.encode('ascii', 'ignore').decode('ascii')

	#Lower case
	text = text.lower()

	#Remove punctuation
	for p in string.punctuation:
		text = text.replace(p, " ")
	

	# Remove additional spaces
	text = re.sub(r'\s+', ' ', text)

	# Remove stop words
	text = " ".join([x for x in text.split() if x not in stopwords.words('english')])
	

	#Lemmatization

	# Load the English language model
	nlp = spacy.load("en_core_web_sm")

	# Process the text
	doc = nlp(text)

	# Perform lemmatization
	text = " ".join([token.lemma_ for token in doc])

	# Filter out words of length less than 3
	text = " ".join([x for x in text.split() if len(x) >= 3])



	return text


# change the value to black
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return "#ffffff"


def create_wordcloud(text):

	frequency = pd.Series(text.split()).value_counts()

	# Create a wordcloud object
	wordcloud = WordCloud(
					    	width=3000, 
					    	height=2000, 
					    	background_color='#136E70', 
					    	max_words=1000,
					    	font_path='Oswald-VariableFont_wght.ttf'
					    	).generate_from_frequencies(frequency)

	# set the word color to black
	wordcloud.recolor(color_func = black_color_func)
	wordcloud.to_file("wordcloud.png")

	return wordcloud






st.sidebar.title("Word Cloud Generator")

text = st.sidebar.text_area(label="Paste your text here", height=300)

button = False

if text:
	button = st.sidebar.button('Generate')

#color = st.sidebar.color_picker("Choose font color", key=1)

if button:
	if text:
		with st.spinner('Cleaning text...'):
			cleaned_text = clean(text)

		with st.spinner("Generating word cloud..."):
			st.success('Text cleaning done!')
			wordcloud = create_wordcloud(cleaned_text)

		st.success('Word Cloud generation done!')
		time.sleep(2)
		st.image("wordcloud.png")
